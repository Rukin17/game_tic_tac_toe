from ttt_game_terminal import valid_move


def test_valid_move():
    abc_list = ['a', 'b', 'c']
    assert valid_move('b1', abc_list) == True
    assert valid_move('n7', abc_list) == False