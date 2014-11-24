import os
from ConfigParser import ConfigParser
from util import get_absolute_path

class Conf(object):

    def get_confs(self):
        confs = {}

        for conf_name in ('agent', 'zk'):
            confs[conf_name] = self.get_conf("%s.conf" % conf_name)

        return confs

    def get_conf(self, conf_name):
        conf_absolute_path = get_absolute_path('conf/')
        conf_file_path = os.path.join(conf_absolute_path, conf_name)

        return self.read_config(conf_file_path)

    def read_config(self, conf_path):
        opts = {}
        confparser = ConfigParser()

        if os.path.exists(conf_path):

            confparser.read(conf_path)
            sections = confparser.sections()

            for section in sections:

                for k, v in confparser.items(section):

                    opts[k] = v
            
        return opts

if __name__ == '__main__':
    conf = Conf()
    opts = conf.get_confs()
    print opts
    

