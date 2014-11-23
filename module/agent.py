import time
import os

from kazoo.client import KazooClient

class Agent(object):

    def run(self):
        zk = KazooClient(hosts="localhost:2181")
        zk.start()

        @zk.DataWatch("/darksteel")
        def watch_data(data, stat):
            print("data are now %s" % data)
            os.system(data)
        
        while 1:
            time.sleep(5)