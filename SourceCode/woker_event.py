import threading
import random
import datetime
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(thread)d] [%(threadName)s]  %(message)s')

def worker(event: threading.Event):
    while not event.wait(3):
        logging.info('running running')

event = threading.Event()
threading.Thread(target=worker, name='printer', args=(event, )).start()

# time.sleep(3)
# event.set()