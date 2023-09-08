from ttt_game_terminal import new_field

def test_new_field():
    assert new_field() == [[' ', 'a', 'b', 'c'], ['1', '_', '_', '_'], ['2', '_', '_', '_'], ['3', '_', '_', '_']]