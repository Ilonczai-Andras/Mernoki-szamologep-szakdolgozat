# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calculus.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculus(object):
    def setupUi(self, Calculus):
        Calculus.setObjectName("Calculus")
        Calculus.resize(800, 580)
        Calculus.setMinimumSize(QtCore.QSize(800, 580))
        Calculus.setMaximumSize(QtCore.QSize(800, 580))
        Calculus.setStyleSheet("QMainWindow {\n"
"            background-color: #2E2E2E;\n"
"        }")
        self.centralwidget = QtWidgets.QWidget(Calculus)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"            background-color: #4E4E4E;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox#comboBox {\n"
"        font-family: \'Courier New\', Courier, monospace;\n"
"        width: 330px;\n"
"        }\n"
"QComboBox QAbstractItemView {\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            background-color: #4E4E4E;\n"
"            selection-background-color: #5E5E5E;\n"
"            color: #FFFFFF;\n"
"        }")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 230, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel#label {\n"
"            background-color: #1C1C1C;\n"
"            font-size: 12pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"        }")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 780, 70))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel#label_2 {\n"
"            background-color: #1C1C1C;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            border: 2px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 10px;\n"
"        }")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 70, 451, 51))
        self.lineEdit.setStyleSheet("QLineEdit#lineEdit {\n"
"            background-color: #1C1C1C;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            font-size: 10pt;\n"
"            width: 35px;\n"
"            height: 30%;\n"
"        }")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 70, 75, 51))
        self.pushButton.setStyleSheet("QPushButton {\n"
"            background-color: #4E4E4E;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            font-size: 10pt;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"            width: 50px;\n"
"            height: 35%;\n"
"        }\n"
"QPushButton:hover {\n"
"            background-color: #5E5E5E;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #6E6E6E;\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 9, 60, 50))
        self.lineEdit_2.setStyleSheet("QLineEdit#lineEdit_2{\n"
"            background-color: #1C1C1C;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            font-size: 10pt;\n"
"            width: 35px;\n"
"            height: 30%;\n"
"        }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 9, 60, 50))
        self.lineEdit_3.setStyleSheet("QLineEdit#lineEdit_2, QLineEdit#lineEdit_3{\n"
"            background-color: #1C1C1C;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            font-size: 10pt;\n"
"            width: 35px;\n"
"            height: 30%;\n"
"        }")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 210, 781, 321))
        self.textBrowser.setObjectName("textBrowser")
        Calculus.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calculus)
        QtCore.QMetaObject.connectSlotsByName(Calculus)

    def retranslateUi(self, Calculus):
        _translate = QtCore.QCoreApplication.translate
        Calculus.setWindowTitle(_translate("Calculus", "MainWindow"))
        self.comboBox.setItemText(0, _translate("Calculus", "Increasing"))
        self.comboBox.setItemText(1, _translate("Calculus", "Strictly Increasing"))
        self.comboBox.setItemText(2, _translate("Calculus", "Decreasing"))
        self.comboBox.setItemText(3, _translate("Calculus", "Strictly Decreasing"))
        self.comboBox.setItemText(4, _translate("Calculus", "Monotonic"))
        self.comboBox.setItemText(5, _translate("Calculus", "Divergent"))
        self.comboBox.setItemText(6, _translate("Calculus", "Limit"))
        self.comboBox.setItemText(7, _translate("Calculus", "Differentiation"))
        self.comboBox.setItemText(8, _translate("Calculus", "Integration"))
        self.label.setText(_translate("Calculus", "Operation:"))
        self.label_2.setText(_translate("Calculus", "Result"))
        self.pushButton.setText(_translate("Calculus", "Enter"))
        self.lineEdit_2.setText(_translate("Calculus", "-10"))
        self.lineEdit_3.setText(_translate("Calculus", "10"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculus = QtWidgets.QMainWindow()
    ui = Ui_Calculus()
    ui.setupUi(Calculus)
    Calculus.show()
    sys.exit(app.exec_())
