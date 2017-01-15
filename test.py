#coding=utf-8
import re

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

print