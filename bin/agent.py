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

def start():
	print 'start'
	agent = Agent()
	agent.loop()

def stop():
	print 'stop'

def status():
	print 'status'

def restart():
	stop()
	start()


if __name__ == '__main__':
    arguments = docopt(__doc__, help=True, version='DarkStell Agent 0.1Beta')

    actionDict = {
    	"start": start,
    	"stop": stop,
    	"status": status,
    	"restart": restart
    }

    for action in actionDict.keys():
    	if arguments[action]:
    		actionDict[action]()

