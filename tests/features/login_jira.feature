Feature: Login to Jira
  As a user,
  I want to login to jira,
  So that I can use the platform.


  Scenario: Valid Login
    Given Jira website is displayed
    When I enter "ucsd.ext10@gmail.com" and "ucsdtest101"
    Then login should be successful