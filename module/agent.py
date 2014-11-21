import signal
import time

class Agent(object):
	def loop(self):

		# def sigterm_stop(signum, frame):
		# 	self._stop = 1

		signal.signal(signal.SIGUSR1, sigterm_stop)
  #       self.auto_auth()
  #       self.node_watcher()
  #       self.loop_tos()
  #       self.get_job()
  #       self.run_job()
  #       self.single_run_job()
  #       self.send_ret()
  #       self.crond_clear_job()
		while 1:
			# if self._stop:
			#     break
			print 111
			time.sleep(5)

