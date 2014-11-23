

def start_daemon(user):

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        sys.stderr.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
        sys.exit(1)
    os.setsid()

    try:
        uinfo = pwd.getpwnam(user)
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


def kill_daemon(pidfile):
    
    try:
        pf = file(pidfile, 'r')
        pid = int(pf.read().strip())
        pf.close()
    except IOError:
        pid = None

    if not pid:
        message = 'pidfile %s does not exist. Daemon not running?\n'
        sys.stderr.write(message % pidfile)
        return

    try:
        times = 1
        while times <= 10:
            os.kill(pid, SIGUSR1)
            time.sleep(2)
            times += 1
        sys.stderr.write("Stop Agent daemon fail,the pid is %d" % pid)
    except OSError, err:
        err = str(err)
        if err.find('No such process') > 0:
            if os.path.exists(pidfile):
                os.remove(pidfile)
        else:
            sys.exit(1)
