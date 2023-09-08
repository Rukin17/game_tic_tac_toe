from ttt_game_terminal import win_check, new_field

def test_win_check():
    field = new_field()
    assert win_check(field, 'X') == None
    field = [[' ', 'a', 'b', 'c'], ['1', 'X', '_', '_'], ['2', '_', 'X', '_'], ['3', '_', '_', 'X']]
    assert win_check(field, 'X') == True