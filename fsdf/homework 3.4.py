x = '!'
o = ' ! '
c = 'Vsem{} {}privet'.format(x,x)
c = c.split()
c = c[-1::-1]
c = ' ! '.join(c)
print(c)

y = f'Vsem{x}{o}{x}privet'
y = y.split()
y = y[-1::-1]
y = ' '.join(y)
print(y)

s = ' ! '.join(input('').split(' ')[::-1])
s = s + " !"
print(s)