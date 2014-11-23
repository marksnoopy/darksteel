#import signal
import time
import os

from kazoo.client import KazooClient

class Agent(object):




	def run(self):

		# def sigterm_stop(signum, frame):
		# 	print 'kill myself'
		#  	self._stop = 1




		def register():
			print 'data modified'

		#signal.signal(signal.SIGUSR1, sigterm_stop)

		zk = KazooClient(hosts='localhost:2181')
		zk.start()


		@zk.DataWatch("/darksteel")
		def watch_children(data, stat):
			print("data are now: %s" % data)
                        os.system(data)

		while 1:

		 	time.sleep(5)

