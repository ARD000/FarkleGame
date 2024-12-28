Feature: Farkle Game

  Scenario: System Loads and Greets the User
    Given the system is started
    When the system loads
    Then I should see a greeting message
    And I should see the message "Reach 10,000 points to win!"
    And I should see the rules of the game printed out

  Scenario: Inputting Player Names
    When the program asks for Player 1's name
    And I input "Test Player 1"
    And the program asks for Player 2's name
    And I input "Test Player 2"
    Then the game should start with Player 1 and Player 2

  Scenario: Game Start
    Given there are two players
    When both players have been named
    Then the game should start
    And Player 1 should roll the dice first

  Scenario: Initial Roll
    Given it is my turn
    When I roll the dice
    Then I should roll six dice
    And the result should be displayed

  Scenario: Understanding the Scoring System
    Given I have rolled the dice
    When I see the results
    Then each die should have a different point value
    And the points should be calculated

  Scenario: Triplets and Higher Combinations
    Given it is my turn
    When I roll 3 or more of the same number
    Then I should see the points calculated based on Farkle rules
    And these points can be banked or I can continue rolling

  Scenario: Banking Points and Continuing to Roll
    Given I have banked 250 points and have 3 dice remaining
    When I roll the remaining 3 dice
    Then any new points or combinations are added to the banked points

  Scenario: Rolling a Farkle
    Given it is my turn
    When I roll the dice
    And none of the remaining dice score points
    Then I should be notified that I Farkled
    And my turn should end immediately

  Scenario: Reaching the Winning Score
    Given I have been playing the game
    And my score is close to the winning score
    When my total score reaches 10,000 points
    Then I should be declared the winner
    And the game should end
    And I should see a congratulatory message
