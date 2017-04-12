#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
from pys import *

def run(size):
    p = Proxy()
    p.size = size
    (http_cnt, https_cnt) = p.createProxyPool(size)
    print 'Fished initializing proxy pool:\n'
    print '%d http proxies; %d https proxies.\n'\
            %(http_cnt, https_cnt)
    print 'Please keep this window open.\n'
    p.autoUpdate()

if __name__ == '__main__':
    run(int(sys.argv[1]))
