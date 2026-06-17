from playwright.sync_api import Page, Locator, expect

class DataIssuesPage:
    def __init__(self, page: Page):
        self.page = page
        # Main application frame and elements
        self.page_frame = page.frame_locator("iframe[title=\"Application Container\"]").frame_locator("iframe[title=\"GenericCRM Application\"]")
        self.issues_toolbar: Locator = self.page_frame.locator('.issues-toolbar')
        self.issues_container: Locator = self.page_frame.locator('[id="issueCardsContainer"]')
        self.issues_item: Locator = self.issues_container.get_by_role('listitem')

    def sfid_original_value(self, row: int):
        item = self.issues_item.nth(row)
        # Targets the last td of the original row
        return item.locator("tr[data-row-type='original'] > td:last-child")
    
    def select_original_cell_issue(self, row: int):
        item = self.issues_item.nth(row)
        # Targets the last td of the original row
        return item.locator("tr[data-row-type='original'] td.cell-issue input[type='radio']")

    def final_cell_issue_value(self, row: int):
        item = self.issues_item.nth(row)
        # Targets the last td of the original row
        return item.locator("tr[data-row-type='final']").get_by_role('button')
