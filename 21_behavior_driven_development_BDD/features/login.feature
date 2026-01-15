Feature: Login
    Identify the visitor and store their data

Scenario: Succesful Login
    Given username and pwd password
    When Log In button clicked
    Then show welcome message
