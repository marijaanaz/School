import pytest
import time

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


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

    time.sleep(3)
    password_input = browser.find_element_by_id("password")
    password_input.click()
    password_input.send_keys("ucsdtest101" + Keys.RETURN)

    time.sleep(8)
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
    time.sleep(8)
    assert browser.title == "Log in to continue - Log in with Atlassian account"





