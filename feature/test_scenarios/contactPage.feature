Feature: Testing contact form

  Scenario: Sending mail with correct data
    Given Contact form page
    When I insert correct data
    Then I send a message
    And I see communicate about it

  Scenario: Sending message with blank fields
    Given Contact form page
    When I leave blank fields
    And I click "WYŚLIJ"
    Then I can't send it
    And I see message that I couldn't do it

  Scenario Outline: Sending message with only one blank field
    Given Contact form page
    When I leave blank "<name_field>" field
    And I click "WYŚLIJ"
    Then I can't send it
    And I see message about it
    And I see which field I should refill
    Examples:
    | name_field      |
    | Imię            |
    | Adres email     |
    | Twoja wiadomość |

  Scenario Outline: Sending message with incorrect email
    Given Contact form page
    When I fill all fields
    And I insert incorrect "<email_address>"
    Then I can't send it
    And I see message about what's wrong
    Examples:
    | email_address |
    | test.test |
    | 12345@  |
    | test@test |