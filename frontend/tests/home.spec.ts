import { test, expect } from '@playwright/test';

test('homepage has title and loads correctly', async ({ page }) => {
  await page.goto('/'); 
  await expect(page.locator('nav')).toBeVisible(); 
});
