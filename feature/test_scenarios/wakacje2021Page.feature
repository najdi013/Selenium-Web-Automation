Feature: Page with info about courses

  #POP-UPs
  Scenario: Szczegóły kursu pop-up appears
    Given I'm on courses page
    When I click "Poznaj szczegóły" button
    Then Pop-up window with "Szczegóły kursu" details appears

  Scenario: Szczgóły kursu closure by "x"
    Given I'm on courses page
    When I click "Poznaj szczegóły" button
    And Pop-up window with "Szczegóły kursu" details appears
    Then I can close it by clicking "x"

  Scenario: Szczgóły kursu closure by clicking outside
    Given I'm on courses page
    When I click "Poznaj szczegóły" button
    And Pop-up window with "Szczegóły kursu" details appears
    Then I can close it by clicking outside the box

  Scenario Outline: "Sprawdź harmonogram" - biologia & chemia
    Given I'm on courses page
    When I click on "<harmonogram>"
    Then I see pop-up with "<harmonogram lekcji>" for each field
    Examples:
    | harmonogram           | harmonogram lekcji        |
    | harmonogram-biologia  | harmonogram biologia png  |
    | harmonogram-chemia    | harmonogram chemia png    |
    | biologia-combined     | harmonogram biologia png  |
    | chemia-combined       | harmonogram chemia png    |

  #Kup teraz
  Scenario Outline: "Kup teraz" for each courses adds course to basket
    Given I'm on courses page
    When I click on "<kup teraz>" button
    Then I add "<course>" to cart
    Examples:
      | kup teraz | course  |
      | biologia-kup  | biologia  |
      | chemia-kup    | chemia    |
      | combo-kup     | both      |

  #Video demo
  Scenario:
    Given I'm on courses page
    When I click on video
    Then It starts playing

  Scenario:
    Given I'm on courses page and video is playing
    When I click on video
    Then It stops playing