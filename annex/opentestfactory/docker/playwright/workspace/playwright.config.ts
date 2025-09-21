import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  reporter: [['list']], // OTF側からreporterを上書き指定できる
});
