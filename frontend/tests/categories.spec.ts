import { test, expect, Page } from "@playwright/test";
import { MappingCategory } from "../utils/types/MappingCategory";
import repositoryResult from "./MockData/repositoryResult.json";

const loadMockRoutes = async (page: Page) => {
  await page.route("*/**/MappingItem/categories/repository*", async (route) => {
    await route.fulfill({ json: repositoryResult });
  });
};

test.describe("Category checks", () => {
  test.beforeEach(async ({ page }) => {
    // Mock the api call before navigating
    await loadMockRoutes(page);
    // Go to the start page before each test.
    await page.goto("/");
  });

  test("All categories available", async ({ page }) => {
    for (const category in MappingCategory) {
      if (isNaN(Number(category))) {
        return;
      }
      await expect(page.getByRole("button", { name: "Repositories", exact: true })).toBeVisible();
    }
  });

  test("Load Category Repositories", async ({ page }) => {
    await page.getByRole("button", { name: "Repositories", exact: true }).click();
    await expect(page.getByRole("link", { name: "GovData - Datenportal für Deutschland", exact: true })).toBeVisible();
  });
});
