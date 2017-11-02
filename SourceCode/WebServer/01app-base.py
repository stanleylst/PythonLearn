# WSGI(规范：1个函数，接受2个参数) Web Server Gateway Interface

import os # 获取本地环境变量
import webob
# from cgi import parse_qs
from webob.dec import wsgify
from webob import Request, Response
from urllib.parse import parse_qs

# def application(environ: dict, start_response):


def hello(request: Request) -> Response:
    name = request.params.get("name", 'anonymous')
    response = webob.Response()
    response.text = 'hello {}'.format(name)
    response.staus_code = 200
    response.content_type = 'text/plain'
    return response


def index(request: Request) -> Response:
    return webob.Response(body='hello world', content_type='text/plain')


router = {
    'hello': hello,
    '/': index
}

@wsgify
def application(request: Request) -> Response:
    return router.get(request.path, index)(request)

#
# @wsgify
# def application(request: webob.Request) -> webob.Response:
#     if request.path == '/hello':   # 手动路由
#         # webob 第三方库实现
#         # request = webob.Request(environ)
#         name = request.params.get("name", 'anonymous')
#
#         response = webob.Response()
#         response.text = 'hello {}'.format(name)
#         response.staus_code = 200
#         response.content_type = 'text/plain'
#         return response
#     return webob.Response(body='hello world', content_type='text/plain')
    # return response(environ, start_response)

    # 自己实现
    # params = parse_qs(environ['QUERY_STRING'])
    # name = params.get('name', ['anonymous'])[0]

    # for k, v in environ.items():
    #     if k not in os.environ.keys():  # 过滤服务端信息
    #         print('{} ==> {}'.format(k, v))
    #
    # start_response('200 ok',[('Content-Type','text/plain')])   # headers
    # return ["hello {}".format(name).encode()]  # 返回bytes的可迭代对象      # body

if __name__ == '__main__':
    from wsgiref.simple_server import make_server  # make_server是标准库提供的容器(窗口用来做协议转化) 这里其实 \
                                                   # 是把HTTP协议转化为WSGI协议
    # 生产环境推荐 gunion 容器
    server = make_server('0.0.0.0', 9000, application)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()