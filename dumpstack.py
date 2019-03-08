#!/usr/bin/python

'''
export top thread of a Java process 
export thread stack of a Java process
usage: python dumpstack.py <pid>
'''

import os
import sys
import re

if len(sys.argv) < 2:
  print 'usage:%s <pid>' % sys.argv[0]
  sys.exit(1)

pid = sys.argv[1]

cmd = 'top -H -p %s -n 1 ' % pid

ps = []
fp = os.popen(cmd)

for x in fp.readlines():
  if 'admin' not in x:
    continue
  x = x.replace('\x1b(B\x1b[m', '').replace('\x1b(B\x1b[m', '')
  xx = re.split('\s+', x.strip())
  xp = '%x' % int(xx[0])
  ps.append((xp, xx[8]))
fp.close()


cmd = 'jstack %s' % pid
fp = os.popen(cmd)
stack = fp.read()
fp.close()

fp = open('top.txt', 'w')
for x, n in ps:
  fp.write('%s,%s\n' % (x, n))
fp.close()

fp = open('jstack.txt', 'w')
fp.write(stack)
fp.close()
