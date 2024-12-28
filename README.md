# Farkle Command-Line Game

An interactive command-line implementation of the classic dice game Farkle, built in Python. This project demonstrates functional programming principles, unit testing with Pytest, and behavior-driven development using Behave.

## Features
- **Gameplay:** Implements Farkle's rules, scoring system, and turn logic.
- **Functional Programming:** Modular, immutable code design.
- **Testing:** Unit tests (`farkle_test.py`) and BDD scenarios (`Behave`).

## How to Run
1. Clone the repository:

## 📋 BDD Features and Scenarios

The project follows **Behavior-Driven Development (BDD)** principles, using Gherkin syntax to define features and test scenarios. The `features` folder contains:

### Features
- **Game Initialization:** Scenarios for starting the game, displaying rules, and setting up players.
- **Gameplay:** Tests for rolling dice, calculating scores, and handling special cases like Farkles.
- **Game Completion:** Validates winning conditions and game-end scenarios.

### Example Gherkin Scenario
```gherkin
Feature: Game Initialization
  As a player,
  I want to start a game of Farkle
  So that I can compete with another player

  Scenario: System Loads and Greets the User
    Given the system is started
    When the system loads
    Then I should see a greeting message
    And I should see the rules of the game printed out
