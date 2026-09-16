import os

from playwright.sync_api import sync_playwright

# Point Playwright to the project's .browsers directory
os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", ".browsers")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com/")
        page.screenshot(path="screenshot.png")
        browser.close()
        print("Screenshot saved to screenshot.png")


if __name__ == "__main__":
    main()
