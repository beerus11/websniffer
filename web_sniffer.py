__author__="Anurag Goel"
# A GUI Client for analysing headers and response of servers/webpages
# Option of choosing Request Type(POST or GET),setting port and timeout
# Save File Dialog is added for saving response and headers as text file
# Add Headers and Add Parameters are not coded Yet.....which will be coded soon...
import sys
import httplib
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

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_url = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.horizontalLayout_2.addWidget(self.lineEdit_url)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_timeout = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_timeout.setObjectName(_fromUtf8("lineEdit_timeout"))
        self.horizontalLayout_3.addWidget(self.lineEdit_timeout)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_port = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.horizontalLayout_3.addWidget(self.lineEdit_port)
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_getresponse = QtGui.QPushButton(self.centralwidget)
        self.btn_getresponse.setObjectName(_fromUtf8("btn_getresponse"))
        self.horizontalLayout.addWidget(self.btn_getresponse)
        self.btn_getheaders = QtGui.QPushButton(self.centralwidget)
        self.btn_getheaders.setObjectName(_fromUtf8("btn_getheaders"))
        self.horizontalLayout.addWidget(self.btn_getheaders)
        self.btn_clear = QtGui.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.horizontalLayout.addWidget(self.btn_clear)
        self.btn_exit = QtGui.QPushButton(self.centralwidget)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout.addWidget(self.btn_exit)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btn_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QObject.connect(self.btn_getresponse, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_response)
        QtCore.QObject.connect(self.btn_getheaders, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_headers)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_response(self):
        url=str(self.lineEdit_url.text())
        if str(self.lineEdit_timeout.text()) == "":
            req_tout=300
        else:
            req_tout=int(str(self.lineEdit_timeout.text()))

        if  str(self.lineEdit_port.text()) == "":
            req_port=80
        else:
            req_port=int(str(self.lineEdit_port.text()))
        conn = httplib.HTTPConnection(url,req_port,timeout=req_tout)
        req_type=self.comboBox.currentText()
        conn.request(req_type, "")
        r1 = conn.getresponse()
        self.textEdit.setPlainText(str(r1.read()))
        conn.close()

    def get_headers(self):
        url=str(self.lineEdit_url.text())
        conn = httplib.HTTPConnection(url)
        conn.request("HEAD", "")
        res = conn.getresponse()
        self.textEdit.setPlainText("Status : "+str(res.status)+"\n"+str(res.reason)+"\n"+"Length :"+str(res.length)+"\n")
        res=res.getheaders()
        for i in res:
            self.textEdit.setPlainText(str(self.textEdit.toPlainText())+str(i)+"\n")
        conn.close()

    def save(self):
        self.filename = QtGui.QFileDialog.getSaveFileName(self.window,str(self.lineEdit_url.text()))
        self.filename=self.filename+'.txt'
        f = open(self.filename, 'wt')
        filedata = self.textEdit.toPlainText()
        f.write(filedata)
        f.close()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Sniffer", None))
        self.label_2.setText(_translate("MainWindow", "URL:", None))
        self.label.setText(_translate("MainWindow", "Request Type :", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "GET", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "POST", None))
        self.pushButton_5.setText(_translate("MainWindow", "Save", None))
        self.pushButton_7.setText(_translate("MainWindow", "Add Parameters", None))
        self.pushButton_6.setText(_translate("MainWindow", "Add Headers", None))
        self.label_3.setText(_translate("MainWindow", "Time Out:", None))
        self.label_4.setText(_translate("MainWindow", "Port:", None))
        self.lineEdit_port.setText(_translate("MainWindow", "80", None))
        self.lineEdit_timeout.setText(_translate("MainWindow", "300", None))
        self.btn_getresponse.setText(_translate("MainWindow", "Get Response", None))
        self.btn_getheaders.setText(_translate("MainWindow", "Get Headers", None))
        self.btn_clear.setText(_translate("MainWindow", "Clear", None))
        self.btn_exit.setText(_translate("MainWindow", "Exit", None))


if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)

mainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())

