import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(thread)d] [%(threadName)s]  %(message)s')

def worker():
    logging.info('starting')
    time.sleep(2)
    logging.info('completed')

if __name__ == '__main__':
    logging.info('starting')

    t1 = threading.Thread(target=worker, name='non-daemon')
    t1.start()

    time.sleep(1)

    t2 = threading.Thread(target=worker, name='daemon', daemon=True)
    t2.start()
    logging.info('completed')