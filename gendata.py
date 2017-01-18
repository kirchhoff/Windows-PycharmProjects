#coding=utf-8
import time
import sys
import random
import string
import re
tlds = ('com', 'edu', 'net', 'org', 'gov')
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效
d=[]
for i in xrange(random.randrange(5, 11)): #在5到11中随机选一个数
    dtint = random.randrange(sys.maxint/2**32)
    dtstr = time.ctime(dtint) #timestamp
    llen = random.randrange(4, 8)
    login = ''.join(random.choice(string.ascii_lowercase) for j in range(llen)) #选llen次小写字母作为登录名
    dlen = random.randrange(llen, 13) #domain长度长一点
    dom = ''.join(random.choice(string.ascii_lowercase) for j in xrange(dlen))
    d.append('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, random.choice(tlds), dtint, llen, dlen))


data = d[0]
print data
patt = r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'

m = re.match(patt, data)
print m.group()

m = re.match(r'^(\w{3})', data) #三个连续字母数字字符为一组
print m.group(1)

m = re.match(r'^(\w){3}', data) #一个字母为一组，并且group1被反复替换，最后成了最后一个字符
print m.group(1)

print re.search(r'\d+-\d+-\d+', data).group()

print re.match(r'.*(\d+-\d+-\d+)', data).group(1) #正则表达式天生是贪婪的，因此.*会尽可能的匹配。

print re.match(r'.*?(\d+-\d+-\d+)', data).group(1) #加上？可以去掉贪婪属性，这个符号可以被用在*，+和？后面



