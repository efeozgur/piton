# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitFrm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(626, 232)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 341, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 20, 81, 101))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.widget1 = QtGui.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(110, 20, 211, 100))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.txtAdi = QtGui.QLineEdit(self.widget1)
        self.txtAdi.setObjectName(_fromUtf8("txtAdi"))
        self.verticalLayout.addWidget(self.txtAdi)
        self.txtSoyadi = QtGui.QLineEdit(self.widget1)
        self.txtSoyadi.setObjectName(_fromUtf8("txtSoyadi"))
        self.verticalLayout.addWidget(self.txtSoyadi)
        self.txtTCNo = QtGui.QLineEdit(self.widget1)
        self.txtTCNo.setObjectName(_fromUtf8("txtTCNo"))
        self.verticalLayout.addWidget(self.txtTCNo)
        self.txtSGKNo = QtGui.QLineEdit(self.widget1)
        self.txtSGKNo.setObjectName(_fromUtf8("txtSGKNo"))
        self.verticalLayout.addWidget(self.txtSGKNo)
        self.btnKaydet = QtGui.QPushButton(self.groupBox)
        self.btnKaydet.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.btnKaydet.setObjectName(_fromUtf8("btnKaydet"))
        self.btnCikis = QtGui.QPushButton(self.groupBox)
        self.btnCikis.setGeometry(QtCore.QRect(150, 140, 75, 23))
        self.btnCikis.setObjectName(_fromUtf8("btnCikis"))
        self.btnKayitSil = QtGui.QPushButton(self.groupBox)
        self.btnKayitSil.setGeometry(QtCore.QRect(240, 170, 75, 23))
        self.btnKayitSil.setObjectName(_fromUtf8("btnKayitSil"))
        self.liste = QtGui.QListWidget(Form)
        self.liste.setGeometry(QtCore.QRect(360, 30, 256, 192))
        self.liste.setObjectName(_fromUtf8("liste"))
        self.txtAdi.raise_()
        self.txtSoyadi.raise_()
        self.txtTCNo.raise_()
        self.txtSGKNo.raise_()
        self.txtSoyadi.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.groupBox.raise_()
        self.liste.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "GroupBox", None))
        self.label.setText(_translate("Form", "Adı", None))
        self.label_2.setText(_translate("Form", "Soyadı", None))
        self.label_3.setText(_translate("Form", "TC NO", None))
        self.label_4.setText(_translate("Form", "SGK NO", None))
        self.btnKaydet.setText(_translate("Form", "KAY&DET", None))
        self.btnCikis.setText(_translate("Form", "ÇIKIŞ", None))
        self.btnKayitSil.setText(_translate("Form", "KAYIT SİL", None))

