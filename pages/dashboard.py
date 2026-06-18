from playwright.sync_api import Page, Locator, expect

class Dashboard:
    def __init__(self, page: Page):
        self.page = page
        # Welcome modal elements
        self.welcome_modal: Locator = page.locator('[id="welcomeModal"]')
        self.modal_title: Locator = self.welcome_modal.locator('[id="modalTitle"]')
        self.got_it_button: Locator = self.welcome_modal.get_by_role("button", name="Got it")
        # Main application frame and elements
        self.page_frame = page.frame_locator("iframe[title=\"Application Container\"]").frame_locator("iframe[title=\"GenericCRM Application\"]")
        self.review_fix_issues_button: Locator = self.page_frame.get_by_role("button", name="Review & Fix Issues")

    def navigate_to_data_issues(self):
        self.review_fix_issues_button.click()
        expect(self.page.get_by_text('Loading issues')).not_to_be_visible()
        # TODO: Replace the fixed timeout with a more robust wait condition that ensures the Data Issues grid is fully loaded before proceeding with the tests.
        #self.page.wait_for_timeout(500)  # Wait for the Data Issues grid to load