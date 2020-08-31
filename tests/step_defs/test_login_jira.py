from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Constants

JIRA_HOME = 'http://ucsd-ext.atlassian.net/'


# Scenarios

scenarios('../features/login_jira.feature')


# Given Steps

@given('Jira website is displayed')
def jira_home(browser):
    browser.get(JIRA_HOME)


# When Steps

@when(parsers.parse('I enter "{username}" and "{password}"'))
def enter_login(browser, username, password):
    username_input = browser.find_element_by_id("username")
    username_input.click()
    username_input.send_keys(username + Keys.RETURN)

    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "password")))
    password_input = browser.find_element_by_id("password")
    password_input.click()
    password_input.send_keys(password + Keys.RETURN)


# Then Steps

@then('login should be successful')
def login_successful(browser):
    while True:
        try:
            dashboard = browser.find_element_by_class_name("aui-page-header-main")
            if dashboard.is_displayed():
                print("login successful")
                break
        except NoSuchElementException:
            print("Login unsuccessful")
