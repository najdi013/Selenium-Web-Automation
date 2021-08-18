Feature: Testing sorting, adding courses to basket, choosing categories

  #Categories
  Scenario Outline: Testing categories
    Given Shop's page
    When I choose categorie "<subject>"
    Then I see courses only from "<subject>"
    And I can change categorie to another one

    Examples:
    | subject |
    | biologia  |
    | chemia  |
    | combo |

  Scenario Outline:
    Given I'm on shop's page
    And I choose categorie of one subject
    When I choose another subject
    Then I can change it and see other categorie

  #Sorting
  """I didn't test other sorting categories because of low number (3) of courses"""
  Scenario: Sorting by price
    Given Shop's page
    When I choose sorting by price: ascending
    Then Courses are in right order

  Scenario: Sorting by price
    Given Shop's page
    When I choose sorting by price: descending
    Then Courses are in right order

  Scenario: Sorting after sorting
    Given Shop's page with sorted courses
    When I sort it in another way
    Then I see sorted courses

  #Adding courses to basket from shop's page
  Scenario: Adding course and checking if it's in basket
    Given Shop's page
    When I click on "Dodaj do koszyka" button
    Then I see chosen course in basket

  Scenario: Adding courses to basket
    Given Shop's page
    When I click on all of "Dodaj do koszyka" button
    Then I see all courses in basket

  Scenario: Adding course to basket, coming back and adding it again
    Given Shop's page
    When When I click on "Dodaj do koszyka" button
    And I have this course in basket
    And Coming back to shop's page
    And I click "Dodaj do koszyka" on this same course again
    Then I can't do it




