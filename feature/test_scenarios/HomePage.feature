Feature: Main page. Checking if everything working ok. Including navigation, bars, buttons etc.

  #REDIRECTIONS

  Scenario Outline: Navigation bar
    Given I go to main page
    When I see navigation bar
    And I can click all of "<elements>"
    Then It redirect me to other "<pages>"
    Examples:
    |elements   | pages                                       |
    |O mnie     | https://biochempro100.pl/#o-mnie            |
    |O kursach  | https://biochempro100.pl/wakacje2021/#opis  |
    |Sklep      | https://biochempro100.pl/sklep/             |
    |Kontakt    | https://biochempro100.pl/#kontakt           |
    |Moje konto | https://biochempro100.pl/moje-konto/        |

  Scenario: : "Dołącz teraz" button
    Given I go to main page
    When I click "Dołącz teraz"
    Then It redirects me to "opis" page

  Scenario Outline: "Co Cię interesuje?" buttons
    Given I go to main page
    When I see "Co Cię interesuje?" section
    And I click "<button>"
    Then It redirects me to "<pages>"
    Examples:
    | button            | pages                                       |
    | kursy wakacyjne   | https://biochempro100.pl/wakacje2021/#opis  |
    | kursy teoretyczne | pass                                        |
    | kursy praktyczne  | pass                                        |
    | pojedyncze lekcje | pass                                        |

  Scenario Outline: Bottom menu - MENU
    Given I go to main page
    When I click "<elements>"
    Then It redirects me to "<pages>"
    Examples:
    | elements      | pages                               |
    | Strona główna | https://biochempro100.pl            |
    | O mnie        | https://biochempro100.pl/#o-mnie    |
    | O kursach     | https://biochempro100.pl/#o-kursach |
    | Sklep         | https://biochempro100.pl/sklep/     |
    | Kontakt       | https://biochempro100.pl/#kontakt   |

  Scenario Outline: Bottom menu - POMOC
    Given I go to main page
    When I click "<elements>"
    Then It redirects me to "<pages>"
    Examples:
    | elements              | pages                                           |
    | Regulamin             | https://biochempro100.pl/szkic/regulamin        |
    | Polityka prywatności  | https://biochempro100.pl/polityka-prywatnosci/  |


  Scenario Outline: Bottom menu - SOCIAL MEDIA
    Given I go to main page
    When I click "<elements>"
    Then It redirects me to "<pages>"
    Examples:
    | elements  | pages                                                     |
    | Instagram | https://www.instagram.com/biochempro100/                  |
    | Facebook  | https://www.facebook.com/Bio-Chem-pro100-100271872323027  |

  #BASKET

  Scenario: Basket
    Given I go to main page
    When I click on basket icon
    Then I see basket side menu
