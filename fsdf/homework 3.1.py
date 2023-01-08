print('Укажите ваше Имя')
x = input()
print('Введите ваш возраст')
y = input()
while y == y:
    if y.isdigit():
        y = int(y)
        if y > 0:
            if y < 10:
                print('Привет,шкет', x)
                y = str(y)
                print('Укажите ваше Имя')
                x = input()
                print('Введите ваш возраст')
                y = input()
            elif y > 0 and y >= 10 and y <= 18:
                print('Как жизнь,', x, '?')
                y = str(y)
                print('Укажите ваше Имя')
                x = input()
                print('Введите ваш возраст')
                y = input()
            elif y > 18 and y < 100:
                print('Что желаете,', x, ('?'))
                y = str(y)
                print('Укажите ваше Имя')
                x = input()
                print('Введите ваш возраст')
                y = input()
            elif y >= 100:
                print(x, ', вы лжете - в наше время столько не живут...')
                y = str(y)
                print('Укажите ваше Имя')
                x = input()
                print('Введите ваш возраст')
                y = input()
        else:
            print('Ошибка, повторите ввод')
            print('Укажите ваше Имя')
            x = input()
            print('Введите ваш возраст')
            y = input()
    else:
        print('Ошибка, повторите ввод')
        print('Укажите ваше Имя')
        x = input()
        print('Введите ваш возраст')
        y = input()
        y = str(y)


