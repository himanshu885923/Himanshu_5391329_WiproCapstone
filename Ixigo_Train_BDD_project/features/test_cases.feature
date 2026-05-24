#Feature: Ixigo Positive and Negative Test Cases
#
#  Scenario: Verify login and trains icon
#    Given user opens ixigo website
#    When user logs in using phone number and otp
#    Then trains icon should be visible
#
#  Scenario: Verify valid train search
#    Given user opens ixigo website
#    When user logs in using phone number and otp
#    And user clicks on trains icon
#    And user searches train using excel data
#    Then train result page should open
#
#  Scenario: Verify available seat booking
#    Given user opens ixigo website
#    When user logs in using phone number and otp
#    And user clicks on trains icon
#    And user searches train using excel data
#    And user selects available seat and clicks book
#    Then passenger page should open
#
#  Scenario: Verify passenger and payment flow
#    Given user opens ixigo website
#    When user logs in using phone number and otp
#    And user clicks on trains icon
#    And user searches train using excel data
#    And user selects available seat and clicks book
#    And user selects or adds passenger
#    And user proceeds to payment
#    Then payment page should be displayed
#
#  Scenario: Verify invalid from station validation
#    Given user opens ixigo website
#    When user logs in using phone number and otp
#    And user clicks on trains icon
#    And user enters invalid from station
#    Then invalid station should not be accepted
#
#  Scenario: Verify empty passenger name validation
#    Given user opens ixigo website
#    When user logs in using phone number and otp
#    And user clicks on trains icon
#    And user searches train using excel data
#    And user selects available seat and clicks book
#    And user tries to save passenger without name
#    Then passenger should not be saved