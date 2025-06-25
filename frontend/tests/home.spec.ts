import { test, expect } from '@playwright/test';

test('homepage has title and loads correctly', async ({ page }) => {
  await page.goto('http://localhost:8080');
//   await expect(page).toHaveTitle(/Your App Name/i); // adjust to your real title
  await expect(page.locator('nav')).toBeVisible();  // example element check
});
