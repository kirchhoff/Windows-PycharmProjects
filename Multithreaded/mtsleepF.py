#coding=utf-8

from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime
lock = Lock()

class CleanOutputSet(set):
    '''
    altering the default printable string representation of a set
    set一般打印出的效果是set([X, Y, Z....])
    '''
    def __str__(self):
        return ', '.join(x for x in self)

loops = (randrange(2, 5) for x in xrange(randrange(3, 7))) #randrange---> Choose a random item from range(start, stop[, step]).
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add("线程"+myname)
    print '[%s] Started %s' % (ctime(), myname)
    lock.release()
    sleep(nsec)
    with lock:
        remaining.remove("线程"+myname)
        print '[%s] Completed %s (%d secs)' % (ctime(), myname, nsec)
        print '      (remaining: %s)' % (remaining or 'NONE')



def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()

