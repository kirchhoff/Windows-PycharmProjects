#coding=utf-8
import urllib2
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen,build_opener as uopen,build_opener

import zlib
REGEX = compile('#([\d,]+) in Books')
AMZN = 'https://amazon.com/dp/'

ISBNs = {
    '0132269937': 'Core python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    print "%s%s" % (AMZN, isbn)
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, sdch, br',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'}

    req = urllib2.Request("%s%s" % (AMZN, isbn), headers=headers)
    page = urllib2.urlopen(req)
    data = page.read()
    page.close()
    gzipped=page.headers.get('Content-Encoding')

    if gzipped:
        data=zlib.decompress(data, 16+zlib.MAX_WBITS)

    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print '- %r ranked %s ' % (ISBNs[isbn], getRanking(isbn))


def _main():
    print 'At ', ctime(), 'on Amazon...'
    for isbn in ISBNs:
       Thread(target=_showRanking, args=(isbn,)).start()


@register
def _atexit():
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    _main()