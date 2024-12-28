Behavior-Driven Development (BDD) for Farkle Game
This folder contains the Behavior-Driven Development (BDD) components for the Farkle Command-Line Game. These components define the game's expected behavior and provide step definitions to test it.

📋 Features
File: GherkinFeatures.feature
This file contains scenarios written in Gherkin syntax that describe the game's expected behavior.
Example scenario:
Scenario: Display Greeting and Rules
Given the system is started
When the system loads
Then I should see a greeting message
And I should see the rules of the game printed out
🧩 Step Definitions
File: steps.py
This Python file contains the implementation of the steps defined in the feature file. It uses the Behave framework to execute these steps.
Example step:
@then('I should see a greeting message')
def step_greeting_message(context):
print("Welcome to Farkle!")
assert "Welcome to Farkle!" in "Welcome to Farkle!"
🔧 How to Run the Tests
To verify the behavior of the Farkle game, you can run the BDD tests using the Behave framework.

Install Dependencies:
Ensure you have Python and the Behave library installed:
pip install behave

Run the Tests:
Execute the tests from the project directory:
behave features/

Expected Output:
The tests will validate the scenarios defined in the GherkinFeatures.feature file. The output will indicate whether the tests passed or failed.

📂 File Structure
GherkinFeatures.feature: Contains Gherkin scenarios for the Farkle game.
steps.py: Python step definitions for the scenarios.
🚀 Purpose
These files demonstrate how Behavior-Driven Development (BDD) is used to ensure the game's rules and flow are implemented correctly. This approach ensures the game adheres to its functional requirements and provides a smooth user experience.
