import signal
import time

from kazoo.client import KazooClient

class Agent(object):


	

	def run(self):

		def sigterm_stop(signum, frame):
			print 'kill myself'
		 	self._stop = 1


		

		def register():
			print 'data modified'

		signal.signal(signal.SIGUSR1, sigterm_stop)

		zk = KazooClient(hosts='10.4.250.38:2181')
		zk.start()
		

		@zk.ChildrenWatch("/")
		def watch_children(children):
			print("Children are now: %s" % children)
    		time.sleep(5)

		while 1:
			children = zk.get_children('/', watch=register)
		    
			time.sleep(5)

