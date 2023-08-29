#!/bin/python3
import os
import shutil

class FilesInstaller:
    def __init__(self):
        self.installed_files = []
        self.installed_dirs = []
        self.force = False
        self.is_bad = False

    def __del__(self):
        if  self.is_bad:
            self.restore_installed()

    def restore_installed(self):
        for file in self.installed_files:
            os.unlink(file)
        for dir_ in reversed(self.installed_dirs):
            os.rmdir(dir_)

    def install_dir(self, dst):
        try:
            os.mkdir(dst)
            self.installed_dirs.append(dst)
        except FileExistsError:
            pass
        except:
            self.is_bad = True
            raise

    def install_file(self, src, dst):
        if not self.force and os.path.exists(dst):
            self.is_bad = True
            raise Exception("File exists [{}]".format(dst))
        shutil.move(src, dst)
        self.installed_files.append(dst)

    def install(self, src_dir, dst_dir):
        for (dir_path, dir_names, file_names) in os.walk(src_dir):
            for dir_name in dir_names:
                self.install_dir(dst_dir + '/' + dir_name)
            for file_name in file_names:
                src = dir_path + '/' + file_name
                prefix = os.path.commonpath([dir_path, src_dir])
                dst_prefix = dir_path[len(prefix):]
                dst = dst_dir + '/' + dst_prefix + '/' + file_name
                self.install_file(src, dst)
    
# installer = FilesInstaller()
# installer.install('/home/qcrg/foo/cxx', '/home/qcrg/foo/cxx2')
