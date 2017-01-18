#coding=utf-8
import re
import os
print re.match("foo.?", "food is food very useful for human").group()
print re.search("s foo.*", "dood is food very useful for human").group()

bt ='bat|bet|bit'
m = re.match(bt, "bat")
if m is not None:
    print m.group()

anyend = '.end'
m = re.match(anyend, "bend")
if m is not None:
    print m.group()

patt314 = '3.14'
pi_patt = '3\.14'

m = re.match(pi_patt, '3.14')
if m is not None:
    print m.group()

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print m.group()
    print m.group(1)
    print m.group(2)
    print m.groups()

m = re.match('ab', 'ab')
print m.group()

m = re.match(r'\babc', 'abc')
print m.group()

print re.findall('car', 'car')
print re.findall('car', 'cc')

print '...'
s = "This and that. "
print re.findall(r'(th\w+) and (th\w+)', s, re.IGNORECASE)
re.finditer(r'(th\w+) and (th\w+)', s, re.I)


print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', "2/20/91")

print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', "2/20/1991")

print re.match(r'''(?x)
\((\d{3})\)
[ ] #space
(\d{3})
-
(\d{4})
''', '(800) 555-1212').groups()
print re.match(r'\(\d{3}\) \d{3}-\d{4}', '(800) 555-1212').group()

print re.sub(r'\((?P<biaozhifu1>\d{3})\) (?P<biaozhifu2>\d{3})-\d{4}', '(\g<biaozhifu2>) \g<biaozhifu1>-xxxx', '(800) 555-12123')

print re.match(r'(?P<xxx>\d{4})', '444233').groupdict()['xxx']

f = os.popen('who', 'r')
for eachline in f:
    print re.split(r'\s\s+|\t', eachline.rstrip())
f.close()

f=os.popen('who', 'r')
for eachline in f:
    print re.split(r'\s\s+', eachline)
f.close()

print re.match(r'[\w.]+', '3.2.3333.22.222.22.2\n').group()

import sys
import time
import random
help(random.choice)
help(random.randrange)
time.ctime(random.randrange(sys.maxint/2**32))

