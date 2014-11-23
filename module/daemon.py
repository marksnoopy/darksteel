
import pwd
import sys
import os
import signal
import time

class Daemon(object):

    def __init__(self, user):
        self.user = user

    def start_daemon(self):

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)
        os.setsid()

        try:
            uinfo = pwd.getpwnam(self.user)
            os.setegid(uinfo.pw_gid)
            os.seteuid(uinfo.pw_uid)
        except KeyError:
            sys.stderr.write("user %s is not valid\n")
            sys.exit(1)

        os.chdir('/')
        os.umask(022)
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)


    def kill_daemon(self):

        #try:
        #    pf = file(pidfile, 'r')
        #    pid = int(pf.read().strip())
        #    pf.close()
        #except IOError:
        #    pid = None
        pid = 3200

        if not pid:
            message = 'pidfile %s does not exist. Daemon not running?\n'
            sys.stderr.write(message % pidfile)
            return

        try:
            os.kill(pid, signal.SIGUSR1)
        except OSError, err:
            err = str(err)
            if err.find('No such process') > 0:
                print err
                #if os.path.exists(pidfile):
                #    os.remove(pidfile)
            else:
                sys.exit(1)
