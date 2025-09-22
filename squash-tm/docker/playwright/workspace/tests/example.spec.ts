import { test, expect } from "@playwright/test";

test("Playwright site has title", async ({ page }) => {
  await page.goto("https://playwright.dev/");
  await expect(page).toHaveTitle(/Playwright/);
});
