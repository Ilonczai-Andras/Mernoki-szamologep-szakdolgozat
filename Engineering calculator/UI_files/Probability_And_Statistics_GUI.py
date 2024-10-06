# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\prob_and_stat.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_Prob_and_Stat(object):
    def setupUi(self, Ui_Prob_and_Stat):
        Ui_Prob_and_Stat.setObjectName("Ui_Prob_and_Stat")
        Ui_Prob_and_Stat.resize(1397, 1141)
        Ui_Prob_and_Stat.setMinimumSize(QtCore.QSize(800, 600))
        Ui_Prob_and_Stat.setWindowOpacity(1.0)
        Ui_Prob_and_Stat.setStyleSheet("background-color: #2E2E2E;")
        self.centralwidget = QtWidgets.QWidget(Ui_Prob_and_Stat)
        self.centralwidget.setStyleSheet("        QWidget#centralwidget {\n"
"            background-color: #2E2E2E;\n"
"        }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("        QComboBox {\n"
"            background-color: #4E4E4E;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("        QLabel {\n"
"            color: #FFFFFF;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"        }")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("        QComboBox {\n"
"            background-color: #4E4E4E;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.mu = QtWidgets.QTextEdit(self.centralwidget)
        self.mu.setMinimumSize(QtCore.QSize(0, 50))
        self.mu.setStyleSheet("        QTextEdit{\n"
"            background-color: #1C1C1C;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.mu.setObjectName("mu")
        self.verticalLayout_4.addWidget(self.mu)
        self.alpha = QtWidgets.QTextEdit(self.centralwidget)
        self.alpha.setMinimumSize(QtCore.QSize(0, 50))
        self.alpha.setStyleSheet("        QTextEdit{\n"
"            background-color: #1C1C1C;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.alpha.setObjectName("alpha")
        self.verticalLayout_4.addWidget(self.alpha)
        self.sigma = QtWidgets.QTextEdit(self.centralwidget)
        self.sigma.setMinimumSize(QtCore.QSize(0, 50))
        self.sigma.setStyleSheet("        QTextEdit{\n"
"            background-color: #1C1C1C;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.sigma.setObjectName("sigma")
        self.verticalLayout_4.addWidget(self.sigma)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lineEdit_2.setStyleSheet("        QTextEdit{\n"
"            background-color: #1C1C1C;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton.setStyleSheet("        QPushButton {\n"
"            background-color: #1C1C1C;\n"
"            font-size: 10pt;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color: #5E5E5E;\n"
"        }\n"
"        QComboBox QAbstractItemView {\n"
"            background-color: #4E4E4E;\n"
"            selection-background-color: #5E5E5E;\n"
"            color: #FFFFFF;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #6E6E6E;\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("        QLabel {\n"
"            color: #FFFFFF;\n"
"            font-family: \'Courier New\', Courier, monospace; /* Monospaced font */\n"
"        }")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.canvaswidget = QtWidgets.QWidget(self.centralwidget)
        self.canvaswidget.setObjectName("canvaswidget")
        self.verticalLayout.addWidget(self.canvaswidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        Ui_Prob_and_Stat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Prob_and_Stat)
        QtCore.QMetaObject.connectSlotsByName(Ui_Prob_and_Stat)

    def retranslateUi(self, Ui_Prob_and_Stat):
        _translate = QtCore.QCoreApplication.translate
        Ui_Prob_and_Stat.setWindowTitle(_translate("Ui_Prob_and_Stat", "Ui_Prob_and_Stat"))
        self.comboBox.setItemText(0, _translate("Ui_Prob_and_Stat", "Probability"))
        self.comboBox.setItemText(1, _translate("Ui_Prob_and_Stat", "Expected value"))
        self.comboBox.setItemText(2, _translate("Ui_Prob_and_Stat", "Entropy"))
        self.comboBox.setItemText(3, _translate("Ui_Prob_and_Stat", "Variancia"))
        self.comboBox.setItemText(4, _translate("Ui_Prob_and_Stat", "Density function"))
        self.comboBox.setItemText(5, _translate("Ui_Prob_and_Stat", "T test"))
        self.comboBox.setItemText(6, _translate("Ui_Prob_and_Stat", "U test"))
        self.label.setText(_translate("Ui_Prob_and_Stat", "Distribution:"))
        self.comboBox_2.setItemText(0, _translate("Ui_Prob_and_Stat", "Normal"))
        self.comboBox_2.setItemText(1, _translate("Ui_Prob_and_Stat", "Geometriai"))
        self.comboBox_2.setItemText(2, _translate("Ui_Prob_and_Stat", "Poisson"))
        self.comboBox_2.setItemText(3, _translate("Ui_Prob_and_Stat", "Logaritmikus"))
        self.comboBox_2.setItemText(4, _translate("Ui_Prob_and_Stat", "Erlang"))
        self.comboBox_2.setItemText(5, _translate("Ui_Prob_and_Stat", "Pareto"))
        self.mu.setPlaceholderText(_translate("Ui_Prob_and_Stat", "μ"))
        self.alpha.setPlaceholderText(_translate("Ui_Prob_and_Stat", "alpha"))
        self.sigma.setPlaceholderText(_translate("Ui_Prob_and_Stat", "σ2"))
        self.pushButton.setText(_translate("Ui_Prob_and_Stat", "Enter"))
        self.label_2.setText(_translate("Ui_Prob_and_Stat", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_Prob_and_Stat = QtWidgets.QMainWindow()
    ui = Ui_Ui_Prob_and_Stat()
    ui.setupUi(Ui_Prob_and_Stat)
    Ui_Prob_and_Stat.show()
    sys.exit(app.exec_())
