#!/usr/bin/env python
'''
connect to test board
'''

import pexpect, sys
from config import *
import logger

def mav_test(testlog=None):
    '''connect to test board'''
    logger.info("CONNECTING TO TEST BOARD")
    logfile = logger.new_tlog("TestBoard")
#    cmd = "strace -f -ttT -s 200 -o %s.trace mavproxy.py --master %s --out 127.0.0.1:14551 --logfile %s" % (logfile, USB_DEV_TEST, logfile)
    cmd = "mavproxy.py --master %s --out 127.0.0.1:14551 --logfile %s" % (USB_DEV_TEST, logfile)
    if REMOTE_MONITOR['test']:
        cmd += " --out %s" % REMOTE_MONITOR['test']
    return pexpect.spawn(cmd, logfile=testlog, timeout=10)

if __name__ == '__main__':
    test = mav_test()
    test.interact()
