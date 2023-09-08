
from unittest import mock

from ttt_game_terminal import moves_values

def test_moves_values():
    with mock.patch('random.randint') as randint_mock:
        randint_mock.return_value = 1
        assert moves_values() == {'user_val': 'O', 'comp_val': 'X'}
        randint_mock.return_value = 0
        assert moves_values() == {'user_val': 'X', 'comp_val': 'O'}
        