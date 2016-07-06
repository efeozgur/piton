# -*- coding: utf-8 -*-

from PyQt4.QtGui import * 
from PyQt4.QtCore import *
import sqlite3 

import sys, kayitFrm

baglan = sqlite3.connect('data.sqlite3')
imlec = baglan.cursor()



class AnaForm(QDialog, kayitFrm.Ui_Form):
    def __init__(self, parent=None, flags=0):
        super(AnaForm, self).__init__()
        self.setupUi(self)
        self.veriOku()
        self.connect(self.btnCikis, SIGNAL("clicked()"), self.cik)        
        self.connect(self.btnKaydet, SIGNAL("clicked()"), self.kayitYaz)
        self.connect(self.btnKayitSil, SIGNAL("clicked()"), self.kayitSil)                
        self.liste.itemClicked.connect(self.kayitBul)
        
    def veriOku(self):
        imlec.execute("select * from kisiler")
        veriler = imlec.fetchall()
        for i in veriler:
            self.liste.addItem(i[0])
        
    def esitle(self):        
        a=self.liste.currentItem().text()
        print(a)
        
    def cik(self):
        sys.exit(0)
    
    def kayitYaz(self):
    
        imlec.execute("insert into kisiler values (?,?,?,?)", (self.txtAdi.text(), self.txtSoyadi.text(), self.txtTCNo.text(), self.txtSGKNo.text()))
        baglan.commit()
        self.liste.clear()
        self.veriOku()        
        baglan.close()
        print("Kayıt yapıldı...!!")
        
        
    def kayitSil(self):
        baglan = sqlite3.connect('data.sqlite3')
        imlec = baglan.cursor()
        imlec.execute("DELETE from kisiler where ad='"+self.txtAdi.text()+"'")
        
        baglan.commit()
        self.liste.clear()
        self.veriOku()
        baglan.close()
        print("Kayıt Silindi")
        
        
    def kayitBul(self):
        self.txtAdi.setText(self.liste.currentItem().text())


app = QApplication(sys.argv)
form = AnaForm()
form.show()
app.exec_()
