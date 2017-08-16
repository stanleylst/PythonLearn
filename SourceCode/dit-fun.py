def d():
    d = {'a': 1, 'b': 2, 'c': 3}
    while True:
        i = input('>>>>')
        if i.strip() == 'quit':
            return
        if i.strip() in d.keys():
            print('i:{} --> v:{}'.format(i, d.get(i, 'unknow key')))
        # TODO


d()
