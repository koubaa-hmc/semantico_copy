import { test, expect } from "@playwright/test";

test("Portal is running", async ({ page }) => {
  await page.goto("/");
  await expect(page).toHaveTitle("HMC Information Portal");
  await expect(page.getByRole("heading", { name: "Information Portal", exact: true })).toBeVisible();
});
