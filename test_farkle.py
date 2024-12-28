import pytest
from collections import Counter
from FarkleGame import calculate_score, gain_score, set_accumulated_points, roll, Player, print_rules
import random

def test_calculate_score_valid():
    assert calculate_score((1, 1, 1, 2, 3, 4)) == (1000, 3)
    assert calculate_score((5, 5, 5, 2, 3, 4)) == (500, 3)
    assert calculate_score((1, 1, 1, 1, 2, 3)) == (1000, 2)
    assert calculate_score((2, 2, 2, 3, 3, 3)) == (500, 0)

def test_calculate_score_invalid():
    assert calculate_score((2, 3, 4, 6, 6, 6)) == (600, 3)
    assert calculate_score((2, 3, 4, 5, 6, 6)) == (50, 5)

def test_calculate_score_single_1s_and_5s():
    assert calculate_score((1, 2, 3, 4, 1, 1)) == (1000, 3)  
    assert calculate_score((5, 2, 3, 4, 5, 5)) == (500, 3) 
    assert calculate_score((1, 1, 5, 2, 3, 4)) == (250, 3)  
    assert calculate_score((1, 5, 5, 2, 3, 4)) == (200, 3)  

def test_calculate_score_special_combinations():
    assert calculate_score((1, 2, 3, 4, 5, 6)) == (1500, 0)  
    assert calculate_score((2, 2, 3, 3, 4, 4)) == (1500, 0)  

def test_calculate_score_no_score():
    assert calculate_score((2, 3, 4, 6, 6, 2)) == (0, 6)

def test_gain_score():
    player = Player(name="TestPlayer", score=100, accumulated_points=True)
    updated_player = gain_score(player, 200)
    assert updated_player.score == 300

def test_set_accumulated_points():
    player = Player(name="TestPlayer", score=100, accumulated_points=False)
    updated_player = set_accumulated_points(player, True)
    assert updated_player.accumulated_points == True

def test_roll():
    random.seed(0)  
    assert roll(6) == (4, 4, 1, 3, 5, 4)
    assert roll(3) == (4, 3, 4)  

def test_player_initialization():
    player = Player(name="TestPlayer")
    assert player.name == "TestPlayer"
    assert player.score == 0
    assert player.accumulated_points == False

def test_accumulated_points_initialization():
    player = Player(name="TestPlayer")
    assert player.accumulated_points == False

def test_player_score_update():
    player = Player(name="TestPlayer", score=0, accumulated_points=True)
    player = gain_score(player, 1000)
    assert player.score == 1000
    player = gain_score(player, 500)
    assert player.score == 1500

def test_print_rules(capsys):
    print_rules()
    captured = capsys.readouterr()
    assert "Welcome to Farkle!" in captured.out
    assert "The objective of the game is to reach 10,000 points." in captured.out

def test_player_initialization_with_non_default_values():
    player = Player(name="TestPlayer", score=500, accumulated_points=True)
    assert player.name == "TestPlayer"
    assert player.score == 500
    assert player.accumulated_points == True

def test_bank_points():
    player = Player(name="TestPlayer", score=0, accumulated_points=True)
    player = gain_score(player, 1000)
    assert player.score == 1000
    player = gain_score(player, 500)
    assert player.score == 1500

def test_farkle_handling():
    player = Player(name="TestPlayer", score=1500, accumulated_points=True)
    roll_score, remaining_dice = calculate_score((2, 3, 4, 6, 6, 2))
    assert roll_score == 0
    assert remaining_dice == 6

if __name__ == "__main__":
    pytest.main()
