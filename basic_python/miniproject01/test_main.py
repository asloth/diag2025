import pytest

from unittest.mock import patch
from main import generate_random_numbers, calculate_distance, game

def test_generate_randon_numbers():
    result = generate_random_numbers()
    assert type(result) == int

@pytest.mark.parametrize(["guess","generated_number","expected"], [(20, 2, 18), (2, 23, 21)])
def test_calculate_distance(guess, generated_number, expected):
    assert calculate_distance(guess, generated_number) == expected

@patch('main.generate_random_numbers', return_value=50)
@patch('main.calculate_distance', return_value=0)
@patch('builtins.input', side_effect=["Alice", 50])  # Player name, then guess
@patch('builtins.print')
def test_game_correct_guess_first_try(mock_print, mock_input, mock_calculate_distance, mock_generate_random):
    """Test when player guesses correctly on first try"""
    # Execute
    game()
        
    # Assert
    mock_generate_random.assert_called_once()
    mock_calculate_distance.assert_called_once_with(50, 50)
    mock_print.assert_any_call("Hola Alice, he generado un número aleatorio entre 1 y 100.")
    mock_print.assert_any_call("Felicitaciones Alice, lo lograste en 1 intentos.")


@patch('main.generate_random_numbers', return_value=50)
@patch('builtins.input', side_effect=["Jose", 0])  # Player name, then guess
@patch('builtins.print')
def test_game_with_zero_input(mock_print, mock_input, mock_generate_random):
    """Test when player inputs zero as a guess"""
    # Execute
    game()
        
    # Assert
    mock_generate_random.assert_called_once()
    mock_print.assert_any_call("No lo lograste a pesar de tratar 1 veces. Mas suerte para otra vez.")


@patch('main.generate_random_numbers', return_value=50)
@patch('builtins.input', side_effect=["Alice", 150,0])  # Player name, then guess
@patch('builtins.print')
def test_game_out_of_range(mock_print, mock_input, mock_generate_random):
    """Test when player inputs a number out of the valid range (1-100)"""
    # Execute
    game()
        
    # Assert
    mock_generate_random.assert_called_once()
    mock_print.assert_any_call("Por favor, ingresa un número entre 1 y 100.")


@patch('main.generate_random_numbers', return_value=50)
@patch('main.calculate_distance', return_value=0)
@patch('builtins.input', side_effect=["Alice", "not_a_number", 50])  # Player name, then invalid guess, then correct guess
@patch('builtins.print')
def test_game_with_input_value_error(mock_print, mock_input, mock_calculate_distance, mock_generate_random):
    """Test when player guesses correctly on first try"""
    # Execute
    game()
        
    # Assert
    mock_generate_random.assert_called_once()
    mock_print.assert_any_call("Entrada inválida. Por favor, ingresa un número entero.")
    mock_calculate_distance.assert_called_once_with(50, 50)
    mock_print.assert_any_call("Felicitaciones Alice, lo lograste en 1 intentos.")
