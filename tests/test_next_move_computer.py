from unittest import mock
from ttt_game_terminal import next_move_computer, new_field

def test_next_move_computer():
    with mock.patch('random.randint') as randint_mock:
        randint_mock.side_effect = [2, 2]
        field = new_field()
        next_move_computer(comp_val='X', occupied_fields=4, field=field)
        assert field[2][2] == 'X'
        randint_mock.side_effect = [1, 1]
        next_move_computer(comp_val='O', occupied_fields=4, field=field)
        assert field[1][1] == 'O'