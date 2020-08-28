from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Constants

JIRA_HOME = 'http://ucsd-ext.atlassian.net/'


# Scenarios

scenarios('../features/logout_jira.feature')


# Given Steps

@given('User is logged in')
def login(browser):
    browser.get(JIRA_HOME)
    username_input = browser.find_element_by_id("username")
    username_input.click()
    username_input.send_keys("ucsd.ext10@gmail.com" + Keys.RETURN)

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "password")))
    password_input = browser.find_element_by_id("password")
    password_input.click()
    password_input.send_keys("ucsdtest101" + Keys.RETURN)

    WebDriverWait(browser, 8).until(EC.title_is("System dashboard - JIRA"))
    assert browser.title == "System dashboard - JIRA"


# When Steps

@when('I log out from platform')
def logout(browser):
    dropdown = browser.find_element_by_css_selector(".css-1nnmhgt")
    dropdown.click()

    logout_button = browser.find_element_by_css_selector(".sc-fgfRvd:nth-child(1) .css-5mekwu")
    logout_button.click()

    submit_button = browser.find_element_by_id("logout-submit")
    submit_button.click()


# Then Steps

@then('log out should be successful')
def logout_successful(browser):
    WebDriverWait(browser, 8).until(EC.title_is("Log in to continue - Log in with Atlassian account"))
    assert browser.title == "Log in to continue - Log in with Atlassian account"
