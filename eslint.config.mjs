import js from '@eslint/js';

export default [
  {
    ignores: ['node_modules/**', '.artifacts/**']
  },
  js.configs.recommended,
  {
    files: ['js/**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'script',
      globals: {
        document: 'readonly'
      }
    }
  }
];
