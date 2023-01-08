print('Укажите ваше Имя')
x = input()
print('Введите ваш возраст')
y = input()
y = (y)
if y.isdigit():
    y = int(y)
    if y > 0:
        if y < 10:
            print('Привет,шкет', x)
        if y > 0 and y >= 10 and y <= 18:
            print('Как жизнь,', x, '?')
        if y > 18 and y < 100:
            print('Что желаете,', x, ('?'))
        if y >= 100:
            print(x, ', вы лжете - в наше время столько не живут...')
    else:
        print('Ошибка, повторите ввод')

else:
    print('Ошибка, повторите ввод')
