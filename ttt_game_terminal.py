import random


def new_field() -> list[list]:
    """ Функция создает игровое поле """
    abc_list = ['a', 'b', 'c']
    field = [['_'] * 4 for i in range(4)]  
    field[0][0] = ' '
    for row in range(1, 4):
        field[row][0] = str(row)

    for col in range(1, 4):
        field[0][col] = abc_list[col - 1]
    return field


def display_board(field) -> str:
    for i in field:
        print(' ' * 10, *i)
    

def start_game(field) -> None:
    """ Функция начала игры """
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    return display_board(field)
    

def moves_values() -> dict:
    """ Функция генерирует случайное значение хода для пользователя и компьютера"""
    move_value = ['X', 'O']
    val_dict = {}
    val_dict['user_val'] = move_value[random.randint(0, 1)]
    if val_dict['user_val'] == 'X':
        val_dict['comp_val'] = 'O'
    else:
        val_dict['comp_val'] = 'X'
    return val_dict


def next_move(row: int, col: int, move_value: str, field) -> None:
    """ Функция заполняет поле значением, по указанным координатам """
    field[row][col] = move_value


def next_move_computer(comp_val: str, occupied_fields: int, field) -> None:
    """ Функция генерирует следующий ход для компьютера """
    row = random.randint(1, 3)
    col = random.randint(1, 3)
    if occupied_fields == 9:
        return None
    elif field[row][col] == '_':
        next_move(row, col, comp_val, field)
    
    else:
        next_move_computer(comp_val, occupied_fields, field)


def valid_move(move: str, abc_list: list) -> bool:
    """ Функция проверяет валидность координатов """
    if int(move[1]) not in range(1, 4) or move[0] not in abc_list:
        print(f'Неправильные координаты поля - {move}')
        return False
    return True


def free_field(move, abc_list:list, field) -> [bool, None]:
    """ Функция проверяет свободно ли поле по заданным координатам """
    if valid_move(move, abc_list):
        row = int(move[1])
        col = abc_list.index(move[0]) + 1
        if field[row][col] == '_':
            return True
        else:
            print(f'Это поле занято! Введите другие координаты')
            return False


def win_check(field, sign) -> [True, None]:
    """ Функция проверяет наличие победного результата"""
    for row in field:
        if row[1] == row[2] == row[3] == sign:
            return True
    for col in range(1, 4):
        if field[1][col] == field[2][col] ==  field[3][col] == sign:
            return True
    if field[1][1] == field[2][2] == field[3][3] == sign:
        return True
    elif field[3][1] == field[2][2] == field[1][3] == sign: 
        return True

def main():
    abc_list = ['a', 'b', 'c']    
    new_game = True
    while True: 
        if new_game:                        # если новая игра
            field = new_field()
            start_game(field)
            values = moves_values()
            user_val, comp_val = values.values()
            rand_move = random.randint(1, 2)
            occupied_fields = 0             # кол-во занятых полей
            if rand_move == 1:
                print("Первым начинает Противник!")
            else:
                print("Первый ход за Вами!")
            new_game = False

        else:                               # иначе игра продолжается
            if rand_move % 2 == 0:          # если ходит пользователь
                while True:                 # в цикле просим ввести пользователя валидные координаты свободного поля
                    move = input(f"Ваш ход! Вы играете '{user_val}' Введите координаты поля(Пример: b1): ")
                    if not free_field(move, abc_list, field=field):
                        continue
                    else:
                        row = int(move[1])
                        col = abc_list.index(move[0]) + 1
                        next_move(row, col, user_val, field)
                        occupied_fields += 1
                        
                        break
                
                for i in field:
                    print(' ' * 10, *i)
                if win_check(field, user_val):
                            print("Вы победили!!!", '\n' * 3)
                            new_game = True
                            continue
            else:                           # иначе ход компьютерf
                next_move_computer(comp_val, occupied_fields, field)
                occupied_fields += 1
                print('Ход противника: ')
                for i in field:
                    print(' ' * 10, *i)
                if win_check(field, comp_val):
                            print("Компьютер победил!!!", '\n' * 3)
                            new_game = True 
                            continue        
            rand_move += 1
            if occupied_fields == 9:
                print('Ничья!!!!!', '\n' * 3)
                new_game = True
        

if __name__ == '__main__':
    main()