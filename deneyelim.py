#coding: utf-8
from PyQt4 import QtCore
from PyQt4 import QtGui

import sys, kayitFrm

class anaForm(QtGui.QDialog, kayitFrm.Ui_Form):
    def __init__(self):
        super(anaForm, self).__init__()
        self.setupUi(self)

app = QtGui.QApplication(sys.argv)
forum = anaForm()
forum.show()
app.exec_()


