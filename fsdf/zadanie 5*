from random import randint
x = randint(0, 100)

user_n = 0
attempt = 0
while True:
    print('я загадал число от 0 до 100, попробуй угадать его')
    user_n = (input('Ваше предположение: '))
    attempt += 1
    if user_n.isdigit():
        user_n = int(user_n)
        if user_n == x:
            print('Поздравляю, в отгадали число:', x, '\n Количество попыток:', attempt)
            break
        elif user_n > x:
            print('Моё число меньше', user_n)
            while user_n != x:
                user_n = (input('Попробуйте еще раз: '))
                attempt += 1
                while True:
                    if user_n.isdigit():
                        user_n = int(user_n)
                        if user_n == x:
                            print('Поздравляю, в отгадали число:', x, '\n Количество попыток:', attempt)
                            break
                        while x % 2 == 0:
                            while user_n != x:
                                print('число четноe')
                                attempt += 1
                                user_n = (input('Попробуйте еще раз: '))
                                while True:
                                    if user_n == x:
                                        print('Поздравляю1, вы отгадали число:', x, '\n Количество попыток:', attempt)
                                        break
                                    if user_n.isdigit():
                                        user_n = int(user_n)
                                        while user_n != x:
                                            attempt += 1
                                            user_n = (input('Попробуйте еще раз: '))
                                            while True:
                                                if user_n.isdigit():
                                                    user_n = int(user_n)
                                                    if user_n != x:
                                                        user_n = (input('Попробуйте еще раз: '))
                                                        continue
                                                    else:
                                                        print('Поздравляю, вы отгадали число:', x,
                                                              '\n Количество попыток:', attempt)
                                                        break
                                                if user_n == x:
                                                    print('Поздравляю, вы отгадали число:', x, '\n Количество попыток:', attempt)
                                                    break
                                                else:
                                                    user_n = (input('Неверный формат ввода. Повторите попытку1: '))
                                        break
                                    else:
                                        user_n = (input('Неверный формат ввода. Повторите попытку: '))
                            break
                        else:
                            print('число нечетноe')
                            attempt += 1
                            user_n = (input('Попробуйте еще раз: '))
                            while True:
                                if user_n == x:
                                    print('Поздравляю, вы отгадали число:', x, '\n Количество попыток:', attempt)
                                    break
                                if user_n.isdigit():
                                    user_n = int(user_n)
                                    while user_n != x:
                                        attempt += 1
                                        user_n = (input('Попробуйте еще раз: '))
                                        while True:
                                            if user_n.isdigit():
                                                user_n = int(user_n)
                                                if user_n != x:
                                                    user_n = (input('Попробуйте еще раз: '))
                                                    continue
                                                else:
                                                    print('Поздравляю, вы отгадали число:', x,
                                                          '\n Количество попыток:', attempt)
                                                    break
                                            if user_n == x:
                                                print('Поздравляю, вы отгадали число:', x, '\n Количество попыток:',
                                                      attempt)
                                                break
                                            else:
                                                user_n = (input('Неверный формат ввода. Повторите попытку1: '))
                                    break
                                else:
                                    user_n = (input('Неверный формат ввода. Повторите попытку: '))

                        break
                    else:
                        user_n = (input('Неверный формат ввода. Повторите попытку: '))

            break
        elif user_n < x:
            print('Моё число больше', user_n)
            while user_n != x:
                user_n = (input('Попробуйте еще раз: '))
                attempt += 1
                while True:
                    if user_n.isdigit():
                        user_n = int(user_n)
                        if user_n == x:
                            print('Поздравляю, вы отгадали число:', x, '\n Количество попыток:', attempt)
                            break
                        while x % 2 == 0:
                            while user_n != x:
                                print('число четноe')
                                attempt += 1
                                user_n = (input('Попробуйте еще раз: '))
                                while True:
                                    if user_n == x:
                                        print('Поздравляю1, в отгадали число:', x, '\n Количество попыток:', attempt)
                                        break
                                    if user_n.isdigit():
                                        user_n = int(user_n)
                                        while user_n != x:
                                            attempt += 1
                                            user_n = (input('Попробуйте еще раз: '))
                                            while True:
                                                if user_n.isdigit():
                                                    user_n = int(user_n)
                                                    if user_n != x:
                                                        user_n = (input('Попробуйте еще раз: '))
                                                        continue
                                                    else:
                                                        print('Поздравляю, в отгадали число:', x,
                                                              '\n Количество попыток:', attempt)
                                                        break
                                                if user_n == x:
                                                    print('Поздравляю, в отгадали число:', x, '\n Количество попыток:',
                                                          attempt)
                                                    break
                                                else:
                                                    user_n = (input('Неверный формат ввода. Повторите попытку1: '))
                                        break
                                    else:
                                        user_n = (input('Неверный формат ввода. Повторите попытку: '))
                            break
                        else:
                            print('число нечетноe')
                            attempt += 1
                            user_n = (input('Попробуйте еще раз: '))
                            while True:
                                if user_n == x:
                                    print('Поздравляю, в отгадали число:', x, '\n Количество попыток:', attempt)
                                    break
                                if user_n.isdigit():
                                    user_n = int(user_n)
                                    while user_n != x:
                                        attempt += 1
                                        user_n = (input('Попробуйте еще раз: '))
                                        while True:
                                            if user_n.isdigit():
                                                user_n = int(user_n)
                                                if user_n != x:
                                                    user_n = (input('Попробуйте еще раз: '))
                                                    continue
                                                else:
                                                    print('Поздравляю, в отгадали число:', x,
                                                          '\n Количество попыток:', attempt)
                                                    break
                                            if user_n == x:
                                                print('Поздравляю, в отгадали число:', x, '\n Количество попыток:',
                                                      attempt)
                                                break
                                            else:
                                                user_n = (input('Неверный формат ввода. Повторите попытку: '))
                                    break
                                else:
                                    user_n = (input('Неверный формат ввода. Повторите попытку: '))

                        break
                    else:
                        user_n = (input('Неверный формат ввода. Повторите попытку: '))

            break
    else:
        print('Неверный формат ввода. Повторите попытку')

