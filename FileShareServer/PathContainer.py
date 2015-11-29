import os.path as osp
import os

CURRENT_DIR = osp.realpath('.')

class PathContainer(object):
    def __init__(self, path):
        self.path = osp.normpath(path)
        self.real_path = osp.realpath(path)
        self.isdir = osp.isdir(self.real_path)
        self.isfile = osp.isfile(self.real_path)
        self.name = osp.basename(self.real_path)
        if self.isdir:
            self.name = self.name + '/'

    def get_dir_contents(self):
        all_paths = os.listdir(self.real_path)
        all_paths = [osp.join(self.path,child_path) for child_path in all_paths]
        all_paths = [PathContainer(child) for child in all_paths]
        if self.real_path != CURRENT_DIR:
            parent = PathContainer(osp.join(self.path,'..'))
            parent.name = '../'
            all_paths.append(parent)
        return all_paths
