import time
import os
import signal

from kazoo.client import KazooClient

class Agent(object):

    def __init__(self):
        self._stop = 0

    def run(self):

        def sigterm_stop(signum, frame):
            print "i am killed"
            self._stop = 1

        signal.signal(signal.SIGUSR1, sigterm_stop)

        zk = KazooClient(hosts="10.4.250.38:2181")
        zk.start()

        @zk.DataWatch("/darksteel")
        def watch_data(data, stat):
            print("data are now %s" % data)
            os.system(data)

        while 1:
            print os.getpid()
            if self._stop:
                break
            time.sleep(3)
