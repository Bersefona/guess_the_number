from random import randint
from checks import choose_limit, game

def start_game():
    print('Добро пожаловать в числовую угадайку.')
    print('Выберите максимальное число для угадывания: ', end = '')
    
    right_n = choose_limit()  # Задание правой границы
    n = randint(1, right_n)   # Загадывание числа
    
    print(f'Мы загадали число от 1 до {right_n}.')
    print('Попробуйте угадать его.')
    
    game(n, right_n)

    # Для рестарта
    print('Желаете сыграть ещё раз? [y/n]')
    choice = input()
    if choice.lower() in ('да', 'yes', 'y', 'д'):
        return start_game()
    else:
        return False


start_game() # Первый запуск игры