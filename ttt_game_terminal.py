from random import randint, random


def new_field() -> list[list[str]]:
    """ Функция создает игровое поле """
    mas = [['_'] * 4 for i in range(4)]  
    mas[0][0] = ' '
    for row in range(1, 4):
        mas[row][0] = row

    for col in range(1, 4):
        mas[0][col] = abc_list[col - 1]
    return mas


def start_game(mas: list[list[str]]) -> None:
    """ Функция начала игры """
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    for i in mas:
        print(' ' * 10, *i)


def moves_values() -> dict:
    """ Функция генерирует значение хода для пользователя и компьютера"""
    move_value = ['X', 'O']
    val_dict = {}
    val_dict['user_val'] = move_value[randint(0, 1)]
    if val_dict['user_val'] == 'X':
        val_dict['comp_val'] = 'O'
    else:
        val_dict['comp_val'] = 'X'
    return val_dict


def next_move(row: int, col: int, move_value: str) -> None:
    """ Функция генерирует ход пользователя """
    mas[row][col] = move_value


def next_move_computer(comp_val: str, occupied_fields: int) -> None:
    """ Функция генерирует следующий ход для компьютера """
    row = randint(1, 3)
    col = randint(1, 3)
    if occupied_fields == 9:
        return None
    elif mas[row][col] == '_':
        mas[row][col] = comp_val 
    
    else:
        next_move_computer(comp_val, occupied_fields)


abc_list = ['a', 'b', 'c']
new_game = True


while True:

    if new_game:
        mas = new_field()
        start_game(mas)
        values = moves_values()
        user_val = values['user_val']
        comp_val = values['comp_val']
        rand_move = randint(1, 2)
        occupied_fields = 0
        if rand_move == 1:
            print("Первым начинает Противник!")
        else:
            print("Первый ход за Вами!")
        new_game = False

    else:
        
        if rand_move % 2 == 0:
            move = input(f"Ваш ход! Вы играете '{user_val}' Введите координаты клетки(Пример: b1): ")
            coor_1 = int(move[1])
            coor_2 = abc_list.index(move[0]) + 1

            if coor_1 not in range(1, 4) or move[0] not in abc_list:
                print(f'Неправильные координаты поля - {move}')

            elif mas[coor_1][coor_2] != '_':
                move = input(f'Это поле занято! Введите другие координаты: ')  # TODO Создать продолжение у этой ветки событий
            else:
                next_move(coor_1, coor_2, user_val)
                occupied_fields += 1

            for i in mas:
                print(' ' * 10, *i)
        else:
            next_move_computer(comp_val, occupied_fields)
            occupied_fields += 1
            print('Ход противника: ')
            for i in mas:
                print(' ' * 10, *i)
            
        rand_move += 1
          