import re
from playwright.sync_api import Page, expect
import pytest

from pages.dashboard import Dashboard
from pages.data_issues import DataIssuesPage


@pytest.fixture(scope='function', autouse=True)
def before_each(page: Page):
    dashboard = Dashboard(page)
    page.goto('/index.html')

    # Welcome modal is displayed.
    expect(dashboard.welcome_modal).to_be_visible()
    expect(dashboard.modal_title).to_have_text('Welcome to GenericCRM')
    # close the welcome modal
    dashboard.got_it_button.click()
    # Navigate to the Data Issues grid 
    dashboard.navigate_to_data_issues()


# Test 1: Navigate to the Data Issues grid
def test_number_of_cards_displayed(page: Page):
    data_issues = DataIssuesPage(page)
    # assert that 10 issue cards are displayed
    expect(data_issues.issues_toolbar).to_have_text('Data Issues 10')
    expect(data_issues.issues_card).to_have_count(10)


# Test 2: Extract and validate all issue data
def test_original_row_contains_a_non_empty_sfid_value(page: Page):
    data_issues = DataIssuesPage(page)
    # each card's original row contains a non-empty sfid value
    number_of_issues = data_issues.issues_card.count()
    for i in range(number_of_issues):
        expect(data_issues.sfid_original_value(i)).not_to_be_empty()


# Test 3: Select a specific issue and change its value
def test_select_original_value_for_issue_column(page: Page):
    data_issues = DataIssuesPage(page)
    card_row = 6
    suggested_value = data_issues.suggested_cell_issue(card_row).text_content()
    original_value = data_issues.original_cell_issue(card_row).text_content()

    expect(data_issues.final_cell_issue(card_row)).to_contain_text(suggested_value)
    # select the **original** value for the 7th card's issue column
    data_issues.original_cell_issue(card_row).click()
    expect(data_issues.final_cell_issue(card_row)).to_contain_text(original_value)


# Test 4: Edit a final row field
def test_edit_issue_value_in_final_row(page: Page):
    data_issues = DataIssuesPage(page)
    card_row = data_issues.find_issue_index_by_sfid('00Qak00000RHtuzEAD')
    suggested_value = data_issues.suggested_cell_issue(card_row).text_content()
    
    expect(data_issues.final_cell_issue(card_row)).to_contain_text(suggested_value)
    # edit the issue column in the final row
    data_issues.final_cell_issue(card_row).click()
    data_issues.final_cell_issue_input(card_row).clear()
    data_issues.final_cell_issue_input(card_row).fill('123 Test Street')
    data_issues.final_cell_issue_input(card_row).press('Enter')
    expect(data_issues.final_cell_issue(card_row)).to_contain_text('123 Test Street')


# Test 5: Checkbox selection count
def test_checkbox_selection(page: Page):
    data_issues = DataIssuesPage(page)
    expect(data_issues.alert_bar).to_be_hidden()

    data_issues.issue_checkbox(0).click()
    data_issues.issue_checkbox(2).click()
    data_issues.issue_checkbox(4).click()
    expect(data_issues.alert_bar).to_be_visible()
    expect(data_issues.alert_bar).to_have_text('3 issue(s) selected')
    # select all
    data_issues.select_all_checkbox.check()
    expect(data_issues.alert_bar).to_have_text('10 issue(s) selected')
    # deselect all
    data_issues.select_all_checkbox.uncheck()
    expect(data_issues.alert_bar).to_be_hidden()
