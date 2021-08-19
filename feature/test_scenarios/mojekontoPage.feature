Feature: Login activities
  """Only negative cases, because I didn't get access to any account and can't create new"""

  Scenario: Login without filling fields
    Given Login page
    When I leave blank fields
    And I click on "ZALOGUJ SIĘ" button
    Then I can't log in

  Scenario Outline: Login with blank
    Given Login page
    When I leave blank "<fields>"
    And I click "ZALOGUJ SIĘ"
    Then I can't log in
    And I see message that I couldn't do it
    Examples:
    | fields      |
    | użytkownik  |
    | hasło       |

  Scenario Outline: Login with incorrect data
    Given Login page
    When I insert inccorect "<użytkownik>" and "<hasło>"
    Then I can't log in
    And I see message that data are incorect
    Examples:
    | użytkownik  | hasło     |
    | 123         | 123       |
    | login       | password  |
    | admin       | admin     |


#lost password
  Scenario: "Nie pamiętasz hasła"
    Given Login page
    When I click on "Nie pamiętasz hasła?"
    Then It redirect me to page about lost password

  Scenario Outline: "Resetuj hasło" with incorrect data
    Given Login page
    When I click on "Nie pamiętasz hasła?"
    And I fill field with inccorect "<email>"
    Then I see message that data are incorrect
    Examples:
    | data                |
    | 12345               |
    | 123@                |
    | test@test           |
    | najdi13@interia.pl  |


