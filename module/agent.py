import time
import os

from kazoo.client import KazooClient

class Agent(object):

    def run(self):
        zk = KazooClient(hosts="192.168.0.107:2181")
        zk.start()

        @zk.DataWatch("/darksteel")
        def watch_data(data, stat):
            print("data are now %s" % data)
            os.system(data)
        
        while 1:
            time.sleep(5)