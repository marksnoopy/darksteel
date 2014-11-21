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

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Agent 2.0')
    print arguments
