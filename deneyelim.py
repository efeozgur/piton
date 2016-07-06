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
        self.mesajKutusu()
        
    def mesajKutusu (self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Programdan çıkmak istiyor musunuz ?")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Uyarı")
        #msg.setDetailedText("Programı gerçekten kapatmak isteyip istemediğinizden emin olmak için açılan diyalog penceresi.")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()        
        if(retval==16384):
            sys.exit(0)
            
        
app = QtGui.QApplication(sys.argv)
forum = anaForm()
forum.show()
app.exec_()


