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
from module.conf import Conf
from module.util import get_current_process_user, get_absolute_path

class Command(Conf):

    def __init__(self):
        self._daemon = Daemon(get_current_process_user())

        conf = Conf()
        self._confs = conf.get_confs()
        self._pidfile = get_absolute_path(self._confs['agent']['pid_file']);


    def start(self):
        self._daemon.start_daemon()
        try:
            agent = Agent()
            self._daemon.set_pidfile(self._pidfile)
            agent.run()
        except KeyboardInterrupt:
            print 'stop agent ing ...'
            stop()

    def stop(self):
        self._daemon.kill_daemon(self._pidfile)

    def status(self):
        print 'status'

    def restart(self):
        self.stop()
        self.start()


if __name__ == '__main__':

    arguments = docopt(__doc__, help=True, version='DarkStell Agent 0.1Beta')

    cmd = Command()
    action_dictionaries = {
        "start": cmd.start,
        "stop": cmd.stop,
        "status": cmd.status,
        "restart": cmd.restart
    }

    # loop the action dictionary
    for action in action_dictionaries.keys():

        # matching action and exec
        if arguments[action]:
          action_dictionaries[action]()
