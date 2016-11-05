# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
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
        Form.resize(324, 251)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 160, 21, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 21, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 220, 51, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.button_regen = QtGui.QPushButton(Form)
        self.button_regen.setGeometry(QtCore.QRect(90, 130, 221, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.button_regen.setFont(font)
        self.button_regen.setObjectName(_fromUtf8("button_regen"))
        self.button_submit = QtGui.QPushButton(Form)
        self.button_submit.setGeometry(QtCore.QRect(10, 190, 301, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName(_fromUtf8("button_submit"))
        self.numberview = QtGui.QLabel(Form)
        self.numberview.setGeometry(QtCore.QRect(10, 100, 71, 41))
        self.numberview.setAlignment(QtCore.Qt.AlignCenter)
        self.numberview.setObjectName(_fromUtf8("numberview"))
        self.text_address = QtGui.QLineEdit(Form)
        self.text_address.setGeometry(QtCore.QRect(60, 10, 251, 20))
        self.text_address.setObjectName(_fromUtf8("text_address"))
        self.text_id = QtGui.QLineEdit(Form)
        self.text_id.setGeometry(QtCore.QRect(60, 40, 251, 20))
        self.text_id.setObjectName(_fromUtf8("text_id"))
        self.text_pw = QtGui.QLineEdit(Form)
        self.text_pw.setGeometry(QtCore.QRect(60, 70, 251, 20))
        self.text_pw.setObjectName(_fromUtf8("text_pw"))
        self.text_idin = QtGui.QLineEdit(Form)
        self.text_idin.setGeometry(QtCore.QRect(110, 100, 201, 20))
        self.text_idin.setObjectName(_fromUtf8("text_idin"))
        self.text_pwin = QtGui.QLineEdit(Form)
        self.text_pwin.setGeometry(QtCore.QRect(30, 160, 281, 20))
        self.text_pwin.setObjectName(_fromUtf8("text_pwin"))
        self.text_response = QtGui.QLineEdit(Form)
        self.text_response.setGeometry(QtCore.QRect(70, 220, 241, 20))
        self.text_response.setObjectName(_fromUtf8("text_response"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.button_regen, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.regenerate)
        QtCore.QObject.connect(self.button_submit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.submit)
        QtCore.QObject.connect(self.text_pwin, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Form.onTextChanged)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "PreEncryption", None))
        self.label.setText(_translate("Form", "PW", None))
        self.label_2.setText(_translate("Form", "ID", None))
        self.label_3.setText(_translate("Form", "Address", None))
        self.label_4.setText(_translate("Form", "FormID", None))
        self.label_5.setText(_translate("Form", "FormPW", None))
        self.label_6.setText(_translate("Form", "Response", None))
        self.button_regen.setText(_translate("Form", "Regenerate", None))
        self.button_submit.setText(_translate("Form", "Submit", None))
        self.numberview.setText(_translate("Form", "IMAGE\n"
"HERE", None))

