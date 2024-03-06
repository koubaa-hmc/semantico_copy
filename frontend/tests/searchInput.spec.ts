import { test, expect, Page } from "@playwright/test";
import searchResult from "./MockData/searchResult.json";

const loadMockRoutes = async (page: Page) => {
  await page.route("*/**/MappingItem/search?searchText=Lithologic*", async (route) => {
    await route.fulfill({ json: searchResult });
  });
};

test.describe.serial("Search Box Functionality", () => {
  test.beforeEach(async ({ page }) => {
    // Mock the api call before navigating
    await loadMockRoutes(page);
    // Go to the start page before each test.
    await page.goto("/");
  });

  test("Search available", async ({ page }) => {
    await page.locator('a:has-text("Search")').click();
    await expect(page.getByPlaceholder("Search")).toBeVisible();
  });

  test("Use Search", async ({ page }) => {
    await page.locator('a:has-text("Search")').click();
    const searchInput = page.getByPlaceholder("Search");
    await searchInput.fill("Lithologic");
    await searchInput.press("Enter");
    await expect(page.getByText("Lithologic classification of geologic map units").first()).toBeVisible();
  });
});
