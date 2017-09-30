d = {'a':1,'b':2,'c':3}
print(d.get('a'))
while True:
    c = input('>> ')
    if c.strip() == 'quit':
        break
    else:
        print('c:{}'.format(c.strip()))
        print(d.get(c.strip()))
        print(d.get(c.strip(),'dddddddd'))

