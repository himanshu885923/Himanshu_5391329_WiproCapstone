Feature: Ixigo Train End To End Booking

  Scenario: Complete train booking flow till payment page
    Given user opens ixigo website
    When user logs in using phone number and otp
    And user clicks on trains icon
    And user searches train using excel data
    And user selects available seat and clicks book
    And user selects or adds passenger
    And user proceeds to payment
    Then payment page should be displayed