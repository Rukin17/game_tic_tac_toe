from ttt_game_terminal import next_move, new_field

def test_next_move():
    field = new_field()
    next_move(row=2, col=2, move_value='X', field=field)
    assert field[2][2] == 'X'
    next_move(row=3, col=1, move_value='O', field=field)
    assert field[3][1] == 'O'