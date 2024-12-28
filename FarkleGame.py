# -*- coding: utf-8 -*-
"""
@author: ammad
"""
import random
from collections import Counter
from dataclasses import dataclass, replace
from typing import Any, Dict, List, Tuple

@dataclass(frozen=True)
class Player:
    name: str
    score: int = 0
    accumulated_points: bool = False

    def __str__(self):
        return f"Player(name='{self.name}', score={self.score})"


def gain_score(player: Player, points: int) -> Player:
    return replace(player, score=player.score + points)

def set_accumulated_points(player: Player, value: bool) -> Player:
    return replace(player, accumulated_points=value)

def print_rules() -> None:
    """
    Prints the rules of the game.
    """
    rules = """
    Welcome to Farkle!
    The objective of the game is to reach 10,000 points.

    Rules:
    1. Each player takes turns to roll six dice.
    2. On your first scoring turn, you must score at least 500 points to start accumulating points.
    3. Once you have started accumulating points, you can add any amount of points in subsequent turns.
    4. If you can't score any points in a roll, you get a FARKLE and lose all points for that turn.
    5. The following combinations score points:

    - Single Dice:
     - Single 1: 100 points
     - Single 5: 50 points

    - Three of a Kind:
     - Three 1s: 1,000 points
     - Three 2s: 200 points
     - Three 3s: 300 points
     - Three 4s: 400 points
     - Three 5s: 500 points
     - Three 6s: 600 points

    - Four of a Kind:
     - Four of any number: 1,000 points

    - Five of a Kind:
     - Five of any number: 2,000 points

    - Six of a Kind:
     - Six of any number: 3,000 points

    - Straight (1-2-3-4-5-6):
     - 1,500 points

    - Three Pairs (e.g., 2-2, 3-3, 4-4):
     - 1,500 points

    - Two Triplets:
     - 2,500 points
    """
    print(rules)

def roll(dice_count: int) -> Tuple[int, ...]:
    return tuple(random.randint(1, 6) for _ in range(dice_count))

def apply_scoring_rules(count: Counter, scoring_rules: Dict[Tuple[int, ...], Any]) -> Tuple[int, Counter, int]:
    score = 0
    temp_count = count.copy()
    used_dice = 0

    for key in sorted(scoring_rules.keys(), key=lambda x: -len(x)):
        while all(temp_count[num] >= key.count(num) for num in key):
            score += scoring_rules[key](temp_count)
            for num in key:
                temp_count[num] -= key.count(num)
            used_dice += len(key)

    return score, temp_count, used_dice

def adjust_for_single_1s_and_5s(count: Counter) -> Tuple[int, int]:
    score = 0
    single_ones = count[1] % 3
    single_fives = count[5] % 3
    score += single_ones * 100
    score += single_fives * 50
    used_dice = single_ones + single_fives

    return score, used_dice

def calculate_score(dice_roll: Tuple[int, ...]) -> Tuple[int, int]:
    count = Counter(dice_roll)

    
    if all(count[d] == 1 for d in range(1, 7)):
        return 1500, 0  
    if len(count) == 3 and all(v == 2 for v in count.values()):
        return 1500, 0  

   
    scoring_rules = {
        (1, 1, 1): lambda _: 1000,
        (2, 2, 2): lambda _: 200,
        (3, 3, 3): lambda _: 300,
        (4, 4, 4): lambda _: 400,
        (5, 5, 5): lambda _: 500,
        (6, 6, 6): lambda _: 600,
        (1, 1, 1, 1): lambda _: 1000,
        (2, 2, 2, 2): lambda _: 1000,
        (3, 3, 3, 3): lambda _: 1000,
        (4, 4, 4, 4): lambda _: 1000,
        (5, 5, 5, 5): lambda _: 1000,
        (6, 6, 6, 6): lambda _: 1000,
        (1, 1, 1, 1, 1): lambda _: 2000,
        (2, 2, 2, 2, 2): lambda _: 2000,
        (3, 3, 3, 3, 3): lambda _: 2000,
        (4, 4, 4, 4, 4): lambda _: 2000,
        (5, 5, 5, 5, 5): lambda _: 2000,
        (6, 6, 6, 6, 6): lambda _: 2000,
        (1, 1, 1, 1, 1, 1): lambda _: 3000,
        (2, 2, 2, 2, 2, 2): lambda _: 3000,
        (3, 3, 3, 3, 3, 3): lambda _: 3000,
        (4, 4, 4, 4, 4, 4): lambda _: 3000,
        (5, 5, 5, 5, 5, 5): lambda _: 3000,
        (6, 6, 6, 6, 6, 6): lambda _: 3000,
    }

    score, temp_count, used_dice = apply_scoring_rules(count, scoring_rules)
    single_score, single_used_dice = adjust_for_single_1s_and_5s(temp_count)
    score += single_score
    used_dice += single_used_dice

    remaining_dice = len(dice_roll) - used_dice

    
    remaining_dice = max(remaining_dice, 0)

    return score, remaining_dice

def display_scores(players: List[Player]) -> None:
    scores = "\n".join(f"{player.name}: {player.score} points" for player in players)
    print(f"\nScores:\n{scores}\n")

def display_roll(dice_values: Tuple[int, ...]) -> None:
    print(f"Dice roll: {dice_values}")

def turn_logic(player: Player, turn_score: int, num_dice: int, first_roll: bool) -> Tuple[Player, bool]:
    if num_dice == 0:
        return gain_score(player, turn_score), True

    input("Press Enter to roll the dice.")
    dice_values = roll(num_dice)
    display_roll(dice_values)
    roll_score, remaining_dice = calculate_score(dice_values)

    if roll_score == 0:
        print("FARKLE! You lose all points for this turn.")
        return player, True

    turn_score += roll_score
    print(f"Roll score: {roll_score}, Turn score: {turn_score}, Remaining dice: {remaining_dice}")

    if first_roll and turn_score < 500 and not player.accumulated_points:
        print("You need at least 500 points to start accumulating points.")
        return turn_logic(player, turn_score, remaining_dice, first_roll)
    else:
        player = set_accumulated_points(player, True)

    while True:
        choice = input("Do you want to bank the points and end your turn (b), or roll the remaining dice (r)? ").lower()
        if choice in ('b', 'r'):
            break
        else:
            print("Invalid choice. Please enter 'b' to bank the points or 'r' to roll the remaining dice.")
    
    if choice == 'b':
        return gain_score(player, turn_score), True
    elif remaining_dice == 0:
        return turn_logic(player, turn_score, 6, False)
    else:
        return turn_logic(player, turn_score, remaining_dice, False)

def player_turn(player: Player) -> Player:
    print(f"\n{player.name}'s turn!")
    updated_player, turn_ended = turn_logic(player, 0, 6, True)
    if not player.accumulated_points and updated_player.score < 500:
        # Reset turn score if the player has not accumulated the required 500 points
        updated_player = Player(player.name, player.score, player.accumulated_points)
    return updated_player

def get_player_names() -> Tuple[str, str]:
    player1_name = ""
    while not player1_name:
        player1_name = input("Enter name of Player 1: ")
        if not player1_name:
            print("Player name cannot be empty. Please enter a valid name.")

    player2_name = ""
    while not player2_name:
        player2_name = input("Enter name of Player 2: ")
        if not player2_name:
            print("Player name cannot be empty. Please enter a valid name.")

    return player1_name, player2_name

def start_game() -> Tuple[bool, Player, Player]:
    player1_name, player2_name = get_player_names()
    player1 = Player(player1_name)
    player2 = Player(player2_name)
    print("Players have been named:")
    print(player1)
    print(player2)
    input("If both players are ready, press Enter to begin...")
    return True, player1, player2