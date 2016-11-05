#-*- coding: utf-8 -*-

import sys
from mainPrg import *
import requests
import keycaptcha
import os

url = 'http://yjham2002.woobi.co.kr/test.php'
payload = {'idf': 'admin', 'pwf': 'admin'}
decoded = ''
current = None;
size = 0

def submitSets(formid, formpw, idinput):
    global decoded, url
    payload = {formid: idinput, formpw: decoded}
    print payload  # Need to be erased
    r = requests.post(url, payload)
    return r.text

def roundOff(code):
    global current
    origin = code + int(current[1])
    if not chr(origin).isalpha(): return code  # return without converting
    if chr(origin).islower():
        if code < ord('a'): code = ord('z') - (ord('a') - code) + 1
        if code > ord('z'): code = ord('a') + (code - ord('z')) - 1
    else:
        if code < ord('A'): code = ord('Z') - (ord('A') - code) + 1
        if code > ord('Z'): code = ord('A') + (code - ord('Z')) - 1
    return code

class MyForm(QtGui.QDialog):

    def __init__(self, parent=None):
        global current;
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.text_address.setText(url)
        self.ui.text_pwin.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.text_id.setText(payload.keys()[0])
        self.ui.text_pw.setText(payload.keys()[1])
        self.ui.text_idin.setText(payload.values()[0])
        # self.ui.text_pwin.setText(payload.values()[1])
        self.ui.text_response.setText("Ready")
        self.regenerate()

    def regenerate(self):
        global current
        temp = keycaptcha.generate_captcha()
        label = self.ui.numberview
        myPixmap = QtGui.QPixmap(temp[0])
        myScaledPixmap = myPixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio)
        label.setPixmap(myScaledPixmap)
        current = temp
        os.unlink(temp[0]);
        return temp

    def submit(self):
        self.ui.text_response.setText\
            (submitSets(formid=str(self.ui.text_id.text()), idinput=str(self.ui.text_idin.text()), formpw=str(self.ui.text_pw.text())))
        return

    def onTextChanged(self):
        global current, decoded, size
        if(len(self.ui.text_pwin.text()) == 0):
            size = 0
            decoded = ''
            return
        elif(len(self.ui.text_pwin.text()) < size):
            size = 0
            decoded = ''
            self.ui.text_pwin.setText('')
            return
        decoder = chr(roundOff(ord(str(self.ui.text_pwin.text()[len(self.ui.text_pwin.text())-1])) - int(current[1])))
        print ('INPUT ' + str(self.ui.text_pwin.text()[len(self.ui.text_pwin.text())-1]) + ' NUMBER ' + current[1] + ' OUTPUT ' + decoder)
        decoded += decoder
        print ('['+decoded+']')
        self.regenerate()
        size = len(self.ui.text_pwin.text())
        return

app = QtGui.QApplication(sys.argv)
myapp = MyForm()
myapp.show()
app.exec_()
