#coding: utf-8
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import QMessageBox

import sys, kayitFrm

class anaForm(QtGui.QDialog, kayitFrm.Ui_Form):
    def __init__(self):
        super(anaForm, self).__init__()
        self.setupUi(self)
        self.btnCikis.clicked.connect(self.cikis)
        
    def cikis(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        
        
app = QtGui.QApplication(sys.argv)
forum = anaForm()
forum.show()
app.exec_()


