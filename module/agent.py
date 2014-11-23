import time
import os
import signal

from kazoo.client import KazooClient

from module.conf import Conf

class Agent(Conf, object):

    def __init__(self):
        self._stop = 0

        conf = Conf()
        self._confs = conf.get_confs()

    def run(self):

        def sigterm_stop(signum, frame):
            print "i am killed"
            self._stop = 1

        signal.signal(signal.SIGUSR1, sigterm_stop)

        zk = KazooClient(hosts=self._confs['zk_servers')
        zk.start()

        @zk.DataWatch(self._confs['zk_root'])
        def watch_data(data, stat):
            print("data are now %s" % data)
            os.system(data)

        while 1:
            print os.getpid()
            if self._stop:
                break
            time.sleep(3)
