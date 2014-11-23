"""Agent Manage

Usage:
  run.py [start | stop | status | restart]

Arguments:
  start         start the agent process
  stop          shutdown the agent proces
  restart       shutdown the agent process if the agent is running and start the agent process
  status        check the agent is run or not
Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt

from module.agent import Agent
from module.daemon import Daemon
from module.util import get_current_process_user

class Command():

    def __init__(self):

      self._daemon = Daemon(get_current_process_user)

    def start():
        self._daemon.start_daemon()
        try:
            agent = Agent()
            agent.run()
            print "[STARTED]"
        except KeyboardInterrupt:
            print 'stop agent ing ...'
            stop()

    def stop():
        self._daemon.kill_daemon()
        print "[STARTED]"

    def status():
        print 'status'

    def restart():
        self.stop()
        self.start()


if __name__ == '__main__':

    arguments = docopt(__doc__, help=True, version='DarkStell Agent 0.1Beta')

    action_dictionaries = {
        "start": start,
        "stop": stop,
        "status": status,
        "restart": restart
    }

    cmd = Command()
    # loop the action dictionary
    for action in action_dictionaries.keys():

        # matching action and exec 
        if arguments[action]:
          cmd.actionDict[action]()
