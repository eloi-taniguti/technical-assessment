from playwright.sync_api import Page, Locator

class DataIssuesPage:
    def __init__(self, page: Page):
        self.page = page
        # Main application frame and elements
        self.page_frame = page.frame_locator("iframe[title=\"Application Container\"]").frame_locator("iframe[title=\"GenericCRM Application\"]")
        self.issues_toolbar: Locator = self.page_frame.locator('.issues-toolbar')
        self.issues_container: Locator = self.page_frame.locator('[id="issueCardsContainer"]')
        self.issues_card: Locator = self.issues_container.get_by_role('listitem')
        self.select_all_checkbox: Locator = self.page_frame.get_by_role('checkbox', name='Select all issues')
        self.alert_bar: Locator = self.page_frame.get_by_role('alert')

    def find_issue_index_by_sfid(self, sfid: str):
        all_issues = self.issues_card.all()
        issue_index = -1
        # Iterate to find the matching 'data-record-id'
        for index, issue in enumerate(all_issues):
            if issue.get_attribute("data-record-id") == sfid:
                issue_index = index
                break 
        return issue_index
        
    def sfid_original_value(self, row: int):
        item = self.issues_card.nth(row)
        # Targets the last td of the original row
        return item.locator("tr[data-row-type='original'] > td:last-child")
    
    def original_cell_issue(self, row: int):
        item = self.issues_card.nth(row)
        # Targets the input radio of the original row
        return item.locator("tr[data-row-type='original'] td.cell-issue input[type='radio']")

    def suggested_cell_issue(self, row: int):
        item = self.issues_card.nth(row)
        # Targets the input radio of the suggested row
        return item.locator("tr[data-row-type='suggested'] td.cell-issue input[type='radio']")

    def final_cell_issue(self, row: int):
        item = self.issues_card.nth(row)
        # Targets the button of the final row
        return item.locator("tr[data-row-type='final']").get_by_role('button')

    def final_cell_issue_input(self, row: int):
        item = self.issues_card.nth(row)
        # Targets the input of the final row
        return item.locator("tr[data-row-type='final']").get_by_role('button').locator('input')

    def issue_checkbox(self, row: int):
        item = self.issues_card.nth(row)
        # Targets the  issue checkbox
        return item.locator(".issue-card-header").get_by_role('checkbox')
