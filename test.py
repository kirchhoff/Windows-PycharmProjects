#coding=utf-8
s = []
l=[]
while True:
    a = raw_input()
    l.append(a)
    for ind,c in enumerate(s):
        if c == a:
            print "number is %d" % (int(ind)+1)
    if a not in s:
        s.append(a)
        print "number is %d" % (len(s))
    print "current s:",s
    print "current l:",l