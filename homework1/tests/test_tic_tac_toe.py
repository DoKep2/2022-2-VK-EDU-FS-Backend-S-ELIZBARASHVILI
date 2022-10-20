import unittest
from unittest.mock import patch

import allure

from homework1.app.exceptions.invalid_move import InvalidMoveException
from homework1.app.models.board import Board
from homework1.cli import TicTacToeGame


class TestTicTacToe(unittest.TestCase):
    horizontal_x_board = ([
        ['x', 'x', 'x'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ])
    vertical_x_board = ([
        ['x', '.', '.'],
        ['x', '.', '.'],
        ['x', '.', '.']
    ])
    diagonal_x_board = ([
        ['x', '.', '.'],
        ['.', 'x', '.'],
        ['.', '.', 'x']
    ])

    diagonal_0_board = ([
        ['0', '.', '.'],
        ['.', '0', '.'],
        ['.', '.', '0']
    ])

    draw_board = ([
        ['x', '0', 'x'],
        ['0', '0', 'x'],
        ['x', 'x', '0']
    ])

    @allure.epic('TicTacToe tests')
    @allure.title('Zero player win')
    @patch('builtins.print')
    @patch('builtins.input', return_value='1 2')
    def test_check_zero_player_win(self, mock_input, mock_print):
        game = TicTacToeGame(Board(self.diagonal_0_board))
        game.start(turn='0')
        mock_print.assert_called_with('Winner winner chicken dinner: 0')

    @allure.epic('TicTacToe tests')
    @allure.title('Horizontally win')
    @patch('builtins.print')
    @patch('builtins.input', return_value='2 2')
    def test_check_horizontally_win(self, mock_input, mock_print):
        game = TicTacToeGame(Board(self.horizontal_x_board))
        game.start()
        mock_print.assert_called_with('Winner winner chicken dinner: x')

    @allure.epic('TicTacToe tests')
    @allure.title('Vertically win')
    @patch('builtins.print')
    @patch('builtins.input', return_value='2 2')
    def test_check_vertically_win(self, mock_input, mock_print):
        game = TicTacToeGame(Board(self.vertical_x_board))
        game.start()
        mock_print.assert_called_with('Winner winner chicken dinner: x')

    @allure.epic('TicTacToe tests')
    @allure.title('Diagonally win')
    @patch('builtins.print')
    @patch('builtins.input', return_value='1 2')
    def test_check_diagonally_win(self, mock_input, mock_print):
        game = TicTacToeGame(Board(self.diagonal_x_board))
        game.start()
        mock_print.assert_called_with('Winner winner chicken dinner: x')

    @allure.epic('TicTacToe tests')
    @allure.title('Draw')
    @patch('builtins.print')
    def test_check_draw(self, mock_print):
        game = TicTacToeGame(Board(self.draw_board))
        self.assertEqual(0, game.board.available_cells)

    @allure.epic('TicTacToe tests')
    @allure.title('Move to not empty cell')
    @patch('builtins.input', return_value='1 1')
    def test_move_to_not_empty_cell(self, mock_input):
        game = TicTacToeGame(Board(self.horizontal_x_board))
        with self.assertRaises(InvalidMoveException):
            game.start()

    @allure.epic('TicTacToe tests')
    @allure.title('Move to not existing cell')
    @patch('builtins.input', return_value='4 4')
    def test_move_to_not_existing_cell(self, mock_input):
        game = TicTacToeGame(Board(self.horizontal_x_board))
        with self.assertRaises(InvalidMoveException):
            game.start()
