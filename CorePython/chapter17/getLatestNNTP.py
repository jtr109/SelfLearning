# !/user/bin/env python

import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = "you'llNeverGuess"

def main():

    try:
        n = nntplib.NNTP(HOST)
        #, user=USER, password=PASS,
    except socket.gaierror, e:
        print 'ERROR: cannot reach host "%s"' % HOST
        print '  ("%s")' % eval(str(e))[1]
        return
    except nntplib.NNTPPermanentError, e:
        print 'ERROR: access denied on "%s"' % HOST
        print '  ("%s")' % str(e)
        return
    print
    #todo: not finished (page:497)
