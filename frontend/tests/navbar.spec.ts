import { test, expect } from '@playwright/test';

test.describe('Navbar', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

test('navbar contains links and can open Categories dropdown', async ({ page }) => {
  await expect(page.getByRole('link', { name: 'Home' })).toBeVisible();
  await expect(page.getByRole('link', { name: 'About' })).toBeVisible();
  await expect(page.locator('.navbar-link', { hasText: 'Categories' })).toBeVisible();
  await page.hover('.navbar-link:text("Categories")');
  const firstCategory = page.locator('.navbar-dropdown .navbar-item').first();
  await expect(firstCategory).toBeVisible();
  await firstCategory.click();
  await expect(page).toHaveURL(/\/category\/.+/);
});

test('should open category dropdown and click first category', async ({ page }) => {
  await page.hover('.navbar-link:text("Categories")');
  const firstCategory = page.locator('.navbar-dropdown .navbar-item').first();
  await expect(firstCategory).toBeVisible();
  await firstCategory.click();
  await expect(page).toHaveURL(/\/category\/.+/);
});

  test('should show cart button and auth links', async ({ page }) => {
    await expect(page.locator('nav')).toContainText('Cart');
    await expect(page.locator('nav')).toContainText('Sign up');
    await expect(page.locator('nav')).toContainText('Log in');
  });

  test('should display footer content', async ({ page }) => {
    await expect(page.locator('footer')).toContainText('Copyright');
  });
});
