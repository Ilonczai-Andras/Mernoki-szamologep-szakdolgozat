# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\egyenlet.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Egyenlet(object):
    def setupUi(self, Egyenlet):
        Egyenlet.setObjectName("Egyenlet")
        Egyenlet.resize(1090, 638)
        Egyenlet.setMinimumSize(QtCore.QSize(800, 600))
        Egyenlet.setAnimated(True)
        Egyenlet.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Egyenlet)
        self.centralwidget.setStyleSheet("        QWidget#centralwidget {\n"
"            background-color: #2E2E2E;\n"
"        }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"            background-color: #1C1C1C;\n"
"            color: #FFFFFF;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox QAbstractItemView {\n"
"            background-color: #4E4E4E;\n"
"            selection-background-color: #5E5E5E;\n"
"            color: #FFFFFF;\n"
"        }")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setStyleSheet("QTextEdit#text_edit{\n"
"            background: #1C1C1C;\n"
"            color: #FFFFFF;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            font-size: 14pt;\n"
"        }\n"
" QTextEdit{\n"
"            background-color: #1C1C1C;\n"
"            color: #FFFFFF;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.text_edit.setObjectName("text_edit")
        self.horizontalLayout.addWidget(self.text_edit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"            background-color: #4E4E4E;\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #5E5E5E;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #6E6E6E;\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel#label_2 {\n"
"            color: #FFFFFF;\n"
"            font-size: 14pt;\n"
"            qproperty-alignment: \'AlignRight | AlignTrailing | AlignVCenter\';\n"
"        }")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.canvaswidget = QtWidgets.QWidget(self.centralwidget)
        self.canvaswidget.setObjectName("canvaswidget")
        self.verticalLayout.addWidget(self.canvaswidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Egyenlet.setCentralWidget(self.centralwidget)

        self.retranslateUi(Egyenlet)
        QtCore.QMetaObject.connectSlotsByName(Egyenlet)

    def retranslateUi(self, Egyenlet):
        _translate = QtCore.QCoreApplication.translate
        Egyenlet.setWindowTitle(_translate("Egyenlet", "Egyenlet"))
        self.comboBox.setItemText(0, _translate("Egyenlet", "Equation"))
        self.comboBox.setItemText(1, _translate("Egyenlet", "System of Equations"))
        self.comboBox.setItemText(2, _translate("Egyenlet", "Fourier Series"))
        self.pushButton.setText(_translate("Egyenlet", "Enter"))
        self.label_2.setText(_translate("Egyenlet", "Erdemény"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Egyenlet = QtWidgets.QMainWindow()
    ui = Ui_Egyenlet()
    ui.setupUi(Egyenlet)
    Egyenlet.show()
    sys.exit(app.exec_())