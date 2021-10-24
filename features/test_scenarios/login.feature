Feature: Validate the login feature

  Background:
    Given Launch browser
    When Open the https://biochempro100.pl/moje-konto/ website
    Then Login form is visible

  Scenario Outline: Login with invalid data
    And Insert username "<username>" and "<password>"
    And Click on the login button
    Then Login failed and invalid input data error is displayed
    Then Close the browser
    Examples:
    | username  | password  |
    | test      | test123   |
    | vcxsdf    | 1234      |
    | 1234      | bvcvc     |

  Scenario: Login with empty username
    And Input password "admin123"
    And Check if username is empty
    And Click on the login button
    Then Login failed and empty username error is displayed
    Then Close the browser

    Scenario: Login with empty password
    And Input username "admin"
    And Check if password is empty
    And Click on the login button
    Then Login failed and empty password error is displayed
    Then Close the browser
