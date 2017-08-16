def command():
    cmds = {}

    def default_fn():
        print('default functions')

    def register(cmd):
        def _register(fn):
            cmds[cmd] = fn
            return fn

        return _register

    def run():
        while True:
            cmd = input('>>>')
            if cmd.strip() == 'quit':
                return
            cmds.get(cmd.strip(), default_fn)()

    return register, run


 @register('hh')
 def hh():
     print('hahhahhhhhhhh')

 run()
