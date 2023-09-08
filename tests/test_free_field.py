from ttt_game_terminal import free_field, new_field

def test_free_field():
    abc_list = ['a', 'b', 'c']
    field = new_field()
    assert free_field('b2', abc_list, field) == True
    field = [[' ', 'a', 'b', 'c'], ['1', '_', '_', '_'], ['2', '_', 'X', '_'], ['3', '_', '_', '_']]
    assert free_field('b2', abc_list, field) == False