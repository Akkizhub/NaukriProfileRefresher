from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="naukri_profile",
        headless=False
    )
    page = browser.new_page()
    page.goto("https://www.naukri.com/nlogin/login")
    input("Log in manually and press Enter...")
    browser.close()
