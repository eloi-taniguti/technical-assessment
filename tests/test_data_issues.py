import re
from playwright.sync_api import Page, expect
import pytest

from pages.dashboard import Dashboard
from pages.data_issues import DataIssuesPage


@pytest.fixture(scope='function', autouse=True)
def before_each(page: Page):
    dashboard = Dashboard(page)
    page.goto('http://localhost:8080/index.html')

    # Welcome modal is displayed.
    expect(dashboard.welcome_modal).to_be_visible()
    expect(dashboard.modal_title).to_have_text('Welcome to GenericCRM')
    # close the welcome modal
    dashboard.got_it_button.click()
    # Navigate to the Data Issues grid 
    dashboard.navigate_to_data_issues()


def test_number_of_cards_displayed(page: Page):
    data_issues = DataIssuesPage(page)
    # assert that 10 issue cards are displayed
    expect(data_issues.issues_toolbar).to_have_text('Data Issues 10')
    expect(data_issues.issues_item).to_have_count(10)


def test_original_row_contains_a_non_empty_sfid_value(page: Page):
    data_issues = DataIssuesPage(page)
    # each card's original row contains a non-empty sfid value
    number_of_issues = data_issues.issues_item.count()
    for i in range(number_of_issues):
        expect(data_issues.sfid_original_value(i)).not_to_be_empty()


def test_select_original_value_for_issue_column(page: Page):
    data_issues = DataIssuesPage(page)
    expect(data_issues.final_cell_issue_value(6)).to_contain_text('(778) 555-6677')
    # select the **original** value for the 7th card's issue column
    data_issues.select_original_cell_issue(6).click()
    expect(data_issues.final_cell_issue_value(6)).to_contain_text('778.555.6677')
