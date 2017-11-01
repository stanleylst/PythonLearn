# WSGI(规范：1个函数，接受2个参数) Web Server Gateway Interface

def application(environ, start_response):
    start_response('200 ok',[('Content-Type','text/plain')])   # headers
    return ["hello world".encode()]  # 返回bytes的可迭代对象      # body

if __name__ == '__main__':
    from wsgiref.simple_server import make_server  # make_server是标准库提供的容器(窗口用来做协议转化) 这里其实 \
                                                   # 是把HTTP协议转化为WSGI协议

    server = make_server('0.0.0.0', 9000, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()