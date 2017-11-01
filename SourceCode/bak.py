import inspect
import functools
import datetime
import time

def cache(exp=0):
    def _cache(fn):
        c = {}
        @functools.wraps(fn)
        def wraps(*args, **kwargs):
            key = []
            ret = fn(*args, **kwargs)
            # TODO 检查key
            sign = inspect.signature(fn).parameters
            for k,v in enumerate(args):
                name = list(sign.keys())[k]
                key.append((name,v))
            key.extend(kwargs.items())
            key = '&'.join(['{}={}'.format(arg, value) for arg, value in key])

            # TODO 过期检查
            tn = datetime.datetime.now().timestamp()
            for k in c.keys():
                ret,timestamp = c[k]
                if exp == 0 or tn - timestamp < exp:
                    print('cache hit,result:{}'.format(ret))
                    return ret

            c[key] = (ret,tn)
            #print(ret)
            print('cache miss')
            return ret
        return wraps
    return _cache

@cache(2)
def add(x,y):
    return x + y

@cache(1)
def sum(p,q):
    #time.sleep(3)
    return p * q

add(1,4)
sum(p=2,q=6)
sum(p=2,q=6)



# # 老师代码
#
# from functools import wraps
# import inspect
# import datetime
#
#
# def cache(exp=0):
#     def _cache(fn):
#         cache = {}
#
#         @wraps(fn)
#         def wrap(*args, **kwargs):
#             # TODO key 如何拼装
#             key = []
#             names = set()
#             params = inspect.signature(fn).parameters
#             print('args:', args)
#             for i, arg in enumerate(args):
#                 name = list(params.keys())[i]
#                 # print('i:{},arg:{},name:{},params.keys:{}'.format(i,arg,name,list(params.keys())))  # 这里忘了args是什么了，解构
#                 key.append((name, arg))
#                 names.add(name)
#             key.extend(kwargs.items())
#             names.update(kwargs.keys())
#             for k, v in params.items():
#                 if k not in names:
#                     key.append((k, v.default))
#             key.sort(key=lambda x: x[0])  # 这种排序方式很赞
#             key = '&'.join(['{}={}'.format(name, arg) for name, arg in key])
#             # print(key)
#             if key in cache.keys():
#                 # TODO 超时检测
#                 ret, timestamp = cache[key]  # 函数解构
#                 if exp == 0 or datetime.datetime.now().timestamp() - timestamp < exp:
#                     print('cache hit')
#                     return ret
#             ret = fn(*args, **kwargs)
#             print('cache:{}'.format(cache))
#             print('cache miss')
#             cache[key] = (ret, datetime.datetime.now().timestamp())
#             return ret
#
#         return wrap
#
#     return _cache
#
#
# @cache(3)
# def add(x, y):
#     return x + y
#
#
# add(2, 4)
aaa
bbb
