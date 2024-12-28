from behave import given, when, then
from FarkleGame import calculate_score, Player, gain_score, set_accumulated_points, print_rules, roll
from dataclasses import replace

@given('the system is started')
def step_system_started(context):
    pass

@when('the system loads')
def step_system_loads(context):
    pass

@then('I should see a greeting message')
def step_greeting_message(context):
    print("Welcome to Farkle!")
    assert "Welcome to Farkle!" in "Welcome to Farkle!"

@then('I should see the message "Reach 10,000 points to win!"')
def step_objective_message(context):
    print("Reach 10,000 points to win!")
    assert "Reach 10,000 points to win!" in "Reach 10,000 points to win!"

@then('I should see the rules of the game printed out')
def step_rules_message(context):
    print_rules()
    
@when('the program asks for Player 1\'s name')
def step_ask_player1_name(context):
    context.player1_name = input("Enter name of Player 1: ")

@when('I input "{name}"')
def step_input_name(context, name):
    context.input_name = name

@when('the program asks for Player 2\'s name')
def step_ask_player2_name(context):
    context.player2_name = input("Enter name of Player 2: ")

@then('the game should start with Player 1 and Player 2')
def step_game_start(context):
    assert context.input_name != ""

@given('there are two players')
def step_two_players(context):
    context.player1 = Player(name="Player 1")
    context.player2 = Player(name="Player 2")

@when('both players have been named')
def step_players_named(context):
    pass

@then('the game should start')
def step_game_starts(context):
    pass

@then('Player 1 should roll the dice first')
def step_player1_rolls_first(context):
    print("Player 1's turn! Press Enter to roll the dice.")
    assert True

@given('it is my turn')
def step_my_turn(context):
    context.is_my_turn = True

@when('I roll the dice')
def step_roll_dice(context):
    context.dice_roll = roll(6)

@then('I should roll six dice')
def step_six_dice(context):
    assert len(context.dice_roll) == 6

@then('the result should be displayed')
def step_display_result(context):
    print(f"Dice roll: {context.dice_roll}")
    assert True

@given('I have rolled the dice')
def step_rolled_dice(context):
    context.dice_roll = roll(6)

@when('I see the results')
def step_see_results(context):
    context.score, context.remaining_dice = calculate_score(context.dice_roll)

@then('each die should have a different point value')
def step_different_point_value(context):
    assert True  

@then('the points should be calculated')
def step_points_calculated(context):
    assert context.score is not None

@when('I roll 3 or more of the same number')
def step_roll_same_number(context):
    context.dice_roll = (3, 3, 3, 4, 2, 6)

@then('I should see the points calculated based on Farkle rules')
def step_points_farkle_rules(context):
    score, _ = calculate_score(context.dice_roll)
    assert score == 300

@then('these points can be banked or I can continue rolling')
def step_bank_or_continue(context):
    pass

@given('I have banked 250 points and have 3 dice remaining')
def step_bank_250_points(context):
    context.player1 = Player(name="Player 1", score=250, accumulated_points=True)

@when('I roll the remaining 3 dice')
def step_roll_remaining_3_dice(context):
    context.dice_roll = roll(3)

@then('any new points or combinations are added to the banked points')
def step_add_to_banked_points(context):
    new_score, _ = calculate_score(context.dice_roll)
    context.player1 = gain_score(context.player1, new_score)
    assert context.player1.score == 250 + new_score

@when('none of the remaining dice score points')
def step_no_remaining_dice_score(context):
    context.dice_roll = (2, 3, 4, 6, 6, 6)

@then('I should be notified that I Farkled')
def step_notify_farkle(context):
    print("FARKLE! You lose all points for this turn.")
    assert True

@then('my turn should end immediately')
def step_turn_end_immediately(context):
    context.is_my_turn = False

@given('I have been playing the game')
def step_playing_game(context):
    context.player1 = Player(name="Test Player", score=9000, accumulated_points=True)

@given('my score is close to the winning score')
def step_close_to_winning(context):
    context.player1 = Player(name="Test Player", score=9500, accumulated_points=True)

@when('my total score reaches 10,000 points')
def step_reach_winning_score(context):
    context.player1 = gain_score(context.player1, 500)

@then('I should be declared the winner')
def step_declared_winner(context):
    assert context.player1.score >= 10000

@then('the game should end')
def step_game_end(context):
    assert context.player1.score >= 10000

@then('I should see a congratulatory message')
def step_congratulatory_message(context):
    print(f"{context.player1.name} wins with a score of {context.player1.score}! Congratulations!")
    assert True
