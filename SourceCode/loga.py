import re
import datetime
import time
import threading
import queue
from collections import namedtuple
from watchdog.events import FileSys

matcher = re.compile(r'(?P<remote>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.*)\] "(?P<request>.*)" (?P<status>\d+) (?P<length>\d+) "(?P<url>.*)" "(?P<ua>.*)" .*')
Request = namedtuple('Request',['method','url','version'])

mapping = {
    'length': int,
    'request': lambda x: Request(*x.split()),
    'status': int,
    'time': lambda x: datetime.datetime.strptime(x,'%d/%b/%Y:%H:%M:%S %z'),
}


class  Loader()


# 数据提取
def extract(line):
    regex = r'(?P<remote>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.*)\] "(?P<request>.*)" (?P<status>\d+) (?P<length>\d+) "(?P<url>.*)" "(?P<ua>.*)" .*'
    m = re.match(regex,line)
    if m:
        ret = m.groupdict()
        return {k:mapping.get(k,lambda x:x)(v) for k,v in ret.items()}  # 这句不大懂 TODO 再理解下
    #         # 上句return可拆解如下：
    #         result = {}
    #         for k,v in ret.items():
    #             result[k] = mapping.get(k,lambda x:x)(v)
    #         return result
    raise Except(line)

# 流式加载数据
def read(f):
    for line in f:
        try:
            yield extract(line)
        except:
            pass

def load(path):
    with open(path) as f:
        while True:
            yield from read(f)
            time.sleep(0.1)

# 该代码缩进太深，看起来不够优雅优化方式如上(分拆为2个函数，调用)
# def load(path):
#     with open(path) as f:
#         while True:
#             for line in f:
#                 try:
#                     yield extract(f.readline())
#                 except:
#                     pass
#         time.sleep(0.1)

# 数据加载 - - 普通的数据加载，新增加的文件无法读取到，优化如上《流式加载数据》
# def load(path):
#     with open(path) as f:
#         try:
#             yield extract(f.readline())
#         except:
#             pass

# 滑动窗口- windows函数
def window(source,handler,interval: int, width: int):
    store = []
    start = datetime.datetime.now()
    while True:
        data = next(source)
        store.append(data)
        current = data['time']
        if start is None:
            start = current
        if (current - start).total_seconds() >= interval:
            start = current
            try:
                handler(store)
            except:
                pass
            dt = current - datetime.timedelta(seconds = width)
            store = [x for x in store if x['time'] > dt]


# 分发
def dispatcher(source):
    analyers = []
    queues = []

    def _source(q):
        while True:
            yield q.get()

    def register(handler,interval,width):
        q = queue.Queue()
        queues.append(q)
        t = threading.Thread(target=window,args=(_source(q),handler,interval,width))
        analyers.append(t)

    def start():
        for t in analyers:
            t.start()
        for item in source:
            print(item)
            for q in queues:
                q.put(item)
    return register, start


def  null_handler(items):
    pass

def status_handler(items):
    if len(items) <= 0:
        return
    status = {}
    for x in items:
        if x['status'] not in status.keys():
            status[x['status']] = 0
        status[x['status']] += 1
    total = sum(x for x in status.values())
    for k,v in status.items():
        print("{} ==> {:2f}%".format(k,v/total * 100))  # 小数据点后两位

if __name__ == '__main__':
    import sys
    register, start = dispatcher(load(sys.argv[1]))
    register(null_handler, 5, 10)
    register(status_handler,5,10)
    start()


## 只能分析已经生成的文件，最新生成的数据是无法读取分析的，因此需要"流式"读取文件






























