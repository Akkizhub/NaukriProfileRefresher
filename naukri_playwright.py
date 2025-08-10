from playwright.sync_api import sync_playwright
import logging
import time
import constants  # Import configuration values

# Setup logging
logging.basicConfig(level=logging.INFO, filename="naukri.log", format="%(asctime)s : %(message)s")

def log_msg(msg):
    print(msg)
    logging.info(msg)

def update_mobile_number():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=constants.USER_DATA_DIR,
            headless=constants.HEADLESS
        )
        page = browser.new_page()
        page.goto(constants.NAUKRI_PROFILE_URL)
        log_msg("Navigated to profile page")

        # Close popup if present
        try:
            page.locator("//*[contains(@class, 'crossIcon')]").click(timeout=5000)
            log_msg("Closed popup")
        except:
            log_msg("No popup to close")

        # Click edit icon
        try:
            page.locator("(//*[contains(@class, 'icon edit')])[1]").click(timeout=5000)
            log_msg("Clicked edit icon")
        except:
            log_msg("Edit icon not found")

        # Update mobile number
        try:
            mobile_input = page.locator('//*[@name="mobile"] | //*[@id="mob_number"]')
            mobile_input.fill(constants.MOBILE)
            log_msg(f"Updated mobile number to {constants.MOBILE}")
        except:
            log_msg("Mobile input not found")

        # Save changes
        try:
            page.locator('//button[@type="submit"][@value="Save Changes"] | //*[@id="saveBasicDetailsBtn"]').click()
            log_msg("Clicked save button")
        except:
            log_msg("Save button not found")

        time.sleep(5)
        browser.close()
        log_msg("Browser closed")

if __name__ == "__main__":
    log_msg("----- Playwright Naukri Update Begin -----")
    update_mobile_number()
    log_msg("----- Playwright Naukri Update End -----")
