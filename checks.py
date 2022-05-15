def choose_limit():
    '''
        Проверка границы для загадывания числа.
    '''
    num = input()
    if num.isdigit() and int(num) > 1:
        return int(num)
    else:
        if not num.isalpha():
            print('Число не может содержать буквы или всякие символы! Попробуйте ввести число еще раз.')
            return choose_limit()
        elif int(num) <= 1:
            print('Правая граница должна быть больше левой. Попробуйте ввести число ещё раз.')
            return choose_limit()
        else:
            return int(num)


def is_valid(num, right_n = 100):
    '''
        Проверка вводимого пользователем числа.
    '''
    return num.isdigit() and int(num) in range(1, right_n + 1)


def is_wish(num, n, count):
    '''
        Функция, которая сравнивает число,
        введённое пользователем, с загаданным числом.
        В случае несовпадения указывает, в какую сторону
        следует двигаться пользователю.
    
    '''
    if num < n:
        return print('Ваше число \033[1mменьше\033[0;0m загаданного, попробуйте еще разок')
    elif num > n:
        return print('Ваше число \033[1mбольше\033[0;0m загаданного, попробуйте еще разок.')
    else:
        print(f'Вы угадали, поздравлем! \nМы действительно загадали число {n}.')
        print(f'Попыток сделано: {count}.')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return


def game(n, right_n = 100):
    '''
        Логика игры.
    '''
    user_n = -1
    count = 0
    while user_n != n:
        user_n = input('Ваше предположение: ')
        if not is_valid(user_n, right_n):
            print(f'Может быть, все-таки введем целое число от 1 до {right_n}?')
            continue
        else:
            user_n = int(user_n)
            count += 1
            is_wish(user_n, n, count)
