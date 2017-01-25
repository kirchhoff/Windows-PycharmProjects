#coding=utf-8

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    with lock:
        print 'Refilling candy...',
        try:
            candytray.release()
        except ValueError:
            print 'full, skipping'
        else:
            print 'OK'

def buy():
    with lock:
        print 'Buying candy...',
        if candytray.acquire(False):
            print 'OK'
        else:
            print 'empty, skipping'


def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))


def _main():
    print 'staring at:', ctime()
    nloops = randrange(2, 6)
    print 'THE CANDY MACHINE (full with %d bars)!' % MAX
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()





@register
def _atexit():
    print 'all done at:', ctime()

if __name__ == '__main__':
    _main()