const fs = require('node:fs');

const sitemap = fs.readFileSync('sitemap.xml', 'utf8');
const allRoutes = [...sitemap.matchAll(/<loc>https?:\/\/[^/]+([^<]*)<\/loc>/g)]
  .map((match) => match[1] || '/')
  .map((route) => route.startsWith('/') ? route : `/${route}`);

const scope = process.env.DESIGN_SCOPE || 'all';
const routes = scope === 'all'
  ? allRoutes
  : scope === 'home'
    ? allRoutes.filter((route) => route === '/')
    : allRoutes.filter((route) => route.startsWith(`/${scope}/`));

module.exports = {
  ci: {
    collect: {
      startServerCommand: 'python3 -m http.server 4173 --bind 127.0.0.1',
      startServerReadyPattern: 'Serving HTTP on',
      url: routes.map((route) => `http://127.0.0.1:4173${route}`),
      numberOfRuns: 1,
      settings: {
        onlyCategories: ['performance', 'accessibility', 'best-practices'],
        chromeFlags: '--headless --no-sandbox'
      }
    },
    upload: {
      target: 'filesystem',
      outputDir: `.artifacts/design-audit/${scope}/lighthouse`
    }
  }
};
