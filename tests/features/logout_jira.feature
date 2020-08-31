Feature: Log out from Jira
  As a user,
  I want to log out from jira,
  So that I can close my session.


  Scenario: Valid Log out
    Given I am logged in
    When I log out from platform
    Then log out should be successful