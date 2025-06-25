import { test, expect } from '@playwright/test';

test.describe('Signup', () => {
  test.beforeEach(async ({ page }) => {
    await page.route('**/api/v1/users/', async route => {
      const jsonResponse = {
        username: 'testuser',
        email: 'testuser@example.com',
        token: 'dummy-token',
      };
      await route.fulfill({
        status: 201,
        contentType: 'application/json',
        body: JSON.stringify(jsonResponse),
      });
    });

    await page.goto('/signup');
  });

  test('User can sign up successfully', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'testuser@example.com');
    await page.fill('input[name="password"]', 'TestPassword123!');
    await page.fill('input[name="password2"]', 'TestPassword123!');
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL(/\/login|\/my-account/);
  });
});
