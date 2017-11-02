# WSGI(规范：1个函数，接受2个参数) Web Server Gateway Interface

import os # 获取本地环境变量
import webob
from webob.dec import wsgify
from webob import Request, Response
from urllib.parse import parse_qs
from webob import exc
import re

class Application:
    ROUTER = []

    @classmethod
    def register(cls, pattern):
        def wrap(handler):
            cls.ROUTER.append((re.compile(pattern), handler))   # 预编译好的正则表达式
            return handler
        return wrap


    @wsgify
    def __call__(self, request: Request) -> Response:   # default_handler优化2
        for pattern, handler in self.ROUTER:
            if pattern.match(request.path):
                return handler(request)
        raise exc.HTTPNotFound('Not Found')
        # try:
        #     return self.ROUTER[request.path](request)
        # except KeyError:
        #     raise exc.HTTPNotFound('not found')

@Application.register('^/hello$')
def hello(request: Request) -> Response:
    name = request.params.get("name", 'anonymous')
    response = webob.Response()
    response.text = 'hello {}'.format(name)
    response.staus_code = 200
    response.content_type = 'text/plain'
    return response


@Application.register('^/$')
def index(request: Request) -> Response:
    return webob.Response(body='hello world', content_type='text/plain')



if __name__ == '__main__':
    from wsgiref.simple_server import make_server  # make_server是标准库提供的容器(窗口用来做协议转化) 这里其实 \
    # 是把HTTP协议转化为WSGI协议
    # 生产环境推荐 gunion 容器
    server = make_server('0.0.0.0', 9000, Application())

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()