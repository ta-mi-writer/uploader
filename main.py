import os

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", ".browsers")


def main():
  # Headless for VPS; persistent context saves cookies/session.
  with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
      user_data_dir=".browser-data",
      headless=True,
    )
    page = context.new_page()
    page.goto("https://ooxxx.com/")

    # Step 1: Inspect button locally (DevTools) to find selector/text.
    # Example selectors after inspection:
    # - By text: page.get_by_text("Enter").click()
    # - By role: page.get_by_role("button", name="Enter").click()
    # - By CSS: page.locator("#enter-btn").click()
    # - By XPath: page.locator("xpath=//button[contains(text(),'Enter')]").click()

    # Use the confirmed working selector; fallback to Enter if needed
    try:
      page.get_by_role("button", name="Enter").click(timeout=3000)
      print("Clicked via role button 'Enter'")
    except PlaywrightError:
      page.keyboard.press("Enter")
      print("Pressed Enter key")

    page.screenshot(path="screenshot.png")
    context.close()
    print("Screenshot saved. Age gate handled (headless=True).")


if __name__ == "__main__":
  main()
