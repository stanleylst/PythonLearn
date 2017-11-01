import threading
import random
import datetime
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(thread)d] [%(threadName)s]  %(message)s')


def worker(event: threading.Event):
    s = random.randint(1,5)
    # time.sleep(s)
    event.wait(s)
    event.set()
    logging.info('sleep {}'.format(s))

def boss(event: threading.Event):
    start = datetime.datetime.now()
    event.wait()
    logging.info('worker exit {}'.format(datetime.datetime.now() - start))

def start():
    event = threading.Event()
    b = threading.Thread(target=boss,args=(event, ), name='boss')
    b.start()
    for x in range(5):
        threading.Thread(target=worker, args=(event, ), name='worker-{}'.format(x)).start()

start()