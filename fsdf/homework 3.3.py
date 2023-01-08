print('Введите целое число')
x = int(input())
c = 0
for i in range(1,x+1):
    i = i**3
    print(i)
    c = c + i
print('сумму кубов:', c)
