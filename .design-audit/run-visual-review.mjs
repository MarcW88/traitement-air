#!/usr/bin/env node

import { chromium } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import { spawn } from 'node:child_process';
import { mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';

const VIEWPORTS = [
  { name: 'desktop', width: 1440, height: 1000 },
  { name: 'mobile', width: 390, height: 844 }
];

function parseArgs(argv) {
  const options = {
    baseUrl: '',
    output: '.artifacts/design-audit/visual',
    port: 4173,
    scope: 'all',
    routes: []
  };

  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    const next = argv[index + 1];
    if (value === '--base-url') options.baseUrl = next, index += 1;
    else if (value === '--output') options.output = next, index += 1;
    else if (value === '--port') options.port = Number(next), index += 1;
    else if (value === '--scope') options.scope = next, index += 1;
    else if (value === '--route') options.routes.push(next), index += 1;
    else if (value === '--help') options.help = true;
    else throw new Error(`Unknown option: ${value}`);
  }

  return options;
}

function normalizeRoute(route) {
  if (!route.startsWith('/')) route = `/${route}`;
  return route.endsWith('/') ? route : `${route}/`;
}

function routeSlug(route) {
  return route.replace(/^\/+|\/+$/g, '').replaceAll('/', '--') || 'home';
}

async function sitemapRoutes(scope) {
  const xml = await readFile('sitemap.xml', 'utf8');
  const routes = [...xml.matchAll(/<loc>https?:\/\/[^/]+([^<]*)<\/loc>/g)]
    .map((match) => normalizeRoute(match[1] || '/'));

  if (scope === 'all') return routes;
  if (scope === 'home') return routes.filter((route) => route === '/');
  return routes.filter((route) => route.startsWith(`/${scope}/`));
}

async function waitForServer(url) {
  for (let attempt = 0; attempt < 80; attempt += 1) {
    try {
      const response = await fetch(url);
      if (response.ok) return;
    } catch {}
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  throw new Error(`Local server did not answer: ${url}`);
}

const options = parseArgs(process.argv.slice(2));
if (options.help) {
  console.log('Usage: run-visual-review.mjs [--scope all|home|renovatie-plannen|renovatieprojecten|verduurzamen|problemen-oplossen|vakman-en-offertes|doe-het-zelf] [--route /path/] [--base-url URL] [--output dir] [--port 4173]');
  process.exit(0);
}

const routes = options.routes.length
  ? options.routes.map(normalizeRoute)
  : await sitemapRoutes(options.scope);

if (!routes.length) throw new Error(`No routes found for scope: ${options.scope}`);

const outputRoot = path.resolve(options.output);
await rm(outputRoot, { recursive: true, force: true });
await mkdir(outputRoot, { recursive: true });

let server;
let baseUrl = options.baseUrl.replace(/\/$/, '');
if (!baseUrl) {
  baseUrl = `http://127.0.0.1:${options.port}`;
  server = spawn('python3', ['-m', 'http.server', String(options.port), '--bind', '127.0.0.1', '--directory', '.'], {
    stdio: ['ignore', 'pipe', 'pipe']
  });
  await waitForServer(`${baseUrl}/`);
}

const report = {
  generatedAt: new Date().toISOString(),
  baseUrl,
  scope: options.scope,
  routes,
  viewports: VIEWPORTS,
  pages: []
};

let browser;
try {
  browser = await chromium.launch({ headless: true });

  for (const viewport of VIEWPORTS) {
    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      reducedMotion: 'reduce'
    });

    for (const route of routes) {
      const page = await context.newPage();
      const consoleErrors = [];
      const pageErrors = [];
      page.on('console', (message) => {
        if (message.type() === 'error') consoleErrors.push(message.text());
      });
      page.on('pageerror', (error) => pageErrors.push(error.message));

      const response = await page.goto(`${baseUrl}${route}`, { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts?.ready);

      const measurements = await page.evaluate(() => ({
        title: document.title,
        horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
        clientWidth: document.documentElement.clientWidth,
        documentHeight: document.documentElement.scrollHeight,
        headingCount: document.querySelectorAll('h1, h2, h3, h4, h5, h6').length,
        h1Count: document.querySelectorAll('h1').length,
        interactiveCount: document.querySelectorAll('a[href], button, input, select, textarea, [tabindex]').length,
        imageCount: document.images.length,
        imagesWithoutAlt: [...document.images].filter((image) => !image.hasAttribute('alt')).length
      }));

      const axe = await new AxeBuilder({ page }).analyze();
      const viewportFolder = path.join(outputRoot, viewport.name);
      await mkdir(viewportFolder, { recursive: true });
      const screenshot = path.join(viewportFolder, `${routeSlug(route)}.png`);
      await page.screenshot({ path: screenshot, fullPage: true, animations: 'disabled' });

      let menuScreenshot = null;
      if (viewport.name === 'mobile') {
        const toggle = page.locator('.menu-toggle');
        if (await toggle.count()) {
          await toggle.first().click();
          menuScreenshot = path.join(viewportFolder, `${routeSlug(route)}--menu-open.png`);
          await page.screenshot({ path: menuScreenshot, fullPage: false, animations: 'disabled' });
        }
      }

      report.pages.push({
        route,
        viewport: viewport.name,
        httpStatus: response?.status() ?? null,
        screenshot: path.relative(process.cwd(), screenshot),
        menuScreenshot: menuScreenshot ? path.relative(process.cwd(), menuScreenshot) : null,
        consoleErrors,
        pageErrors,
        axeViolations: axe.violations,
        axeViolationCount: axe.violations.length,
        ...measurements
      });

      await page.close();
    }

    await context.close();
  }
} finally {
  if (browser) await browser.close();
  if (server) server.kill('SIGTERM');
}

await writeFile(path.join(outputRoot, 'report.json'), `${JSON.stringify(report, null, 2)}\n`);
console.log(`Captured ${report.pages.length} rendered page/viewport combinations.`);
console.log(`Report: ${path.join(outputRoot, 'report.json')}`);
