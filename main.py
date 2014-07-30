#!/bin/python3

import sys
from PyQt4 import QtGui, QtCore
import mainWindows
import shutil
import glob
import os
import time
import re
from datetime import datetime

save = './save/'
save_max = 5

class dirCopy():
    def __init__(self):
        self.l_dir = []
    def add_dir(self, name):
        self.l_dir.append(name)
    def delete(self, name):
        try:
            self.l_dir.remove(name)
        except:
            pass
    def copy_rec_dir(self, ndir, files):
        name = ndir + files.split('/')[-1] + '/'
        os.makedirs(name)
        d = glob.glob(files + '/*')
        for f in d:
            if (os.path.isdir(f)):
                self.copy_rec_dir(name, f)
            else:
                shutil.copy2(f, name + f.split('/')[-1])
    def find_oldest_folder(self, l_date):
        l_datetime = []
        for d in l_date:
            d_split = d[0].split('_')
            year = int(d_split[0].split('-')[2])
            month = int(d_split[0].split('-')[1])
            day = int(d_split[0].split('-')[0])
            hour = int(d_split[1].split(':')[0])
            minute = int(d_split[1].split(':')[1])
            l_datetime.append(datetime(year, month, day, hour, minute))
        return (min(l_datetime))
    def remove_old_folder(self):
        l_file = glob.glob(save + '/*')
        l_date = []
        for f in l_file:
            if (len(re.findall('\d+-\d+-\d+_\d+:\d+', f)) > 0):
                l_date.append(re.findall('\d+-\d+-\d+_\d+:\d+', f))
        while (len(l_date) > save_max):
            date = self.find_oldest_folder(l_date)
            day = str(date.day) if date.day > 9 else '0' + str(date.day)
            month = str(date.month) if date.month > 9 else '0' + str(date.month)
            hour = str(date.hour) if date.hour > 9 else '0' + str(date.hour)
            minute = str(date.minute) if date.minute > 9 else '0' + str(date.minute)
            sup = '{0}-{1}-{2}_{3}:{4}'.format(day, month, date.year, hour, minute)
            l_date.remove([sup])
            shutil.rmtree(save + sup)
    def copy(self):
        if (os.path.exists(save) == False or os.path.isdir(save) == False):
            os.makedirs(save)
        name_dir = save + time.strftime('/%d-%m-%Y_%H:%M/', time.localtime())
        try:
            os.makedirs(name_dir)
        except:
            pass
        l_file = []
        for f in self.l_dir:
            if (os.path.exists(f)):
                if (os.path.isfile(f)):
                    shutil.copy2(f, name_dir + f.split('/')[-1])
                elif (os.path.isdir(f)):
                    self.copy_rec_dir(name_dir, f)
        self.remove_old_folder()

    @property
    def getdir(self):
        return (self.l_dir)

class MainViewer(QtGui.QMainWindow, mainWindows.Ui_MainWindow):
    def __init__(self, app, parent=None):
        super(MainViewer, self).__init__(parent)
        self.setupUi(self)
        self.gere_event()
        self.cpy = dirCopy()
    def gere_event(self):
        self.Add.clicked.connect(self.add)
        self.Remove.clicked.connect(self.remove)
        self.Print.clicked.connect(self.print_dir)
        self.Save.clicked.connect(self.save)
    def add(self):
        if (os.path.exists(self.Path.text())):
            self.cpy.add_dir(self.Path.text())
        else:
            print ("file or doesn't exist")
    def remove(self):
        self.cpy.delete(self.Path.text())
    def save(self):
        self.cpy.copy()
    def print_dir(self):
        print (self.cpy.getdir)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainViewer = MainViewer(app)
    mainViewer.show()
    app.exec_()
