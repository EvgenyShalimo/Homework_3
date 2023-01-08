print('Введите целое число')
n = int(input())
c = 0
print('Возвение в куб:')
while n >= 1:
    n = n - 1
    b = (n+1) ** 3
    print(b)
    c = c+b
print(c,'сумма кубов')

