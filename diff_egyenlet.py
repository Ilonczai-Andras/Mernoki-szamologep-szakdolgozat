from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit
from sympy import pretty, symbols, Function, Eq, diff, dsolve
from sympy.parsing.sympy_parser import parse_expr


class Ui_Diff_Egyenlet(object):

    def show_diff_equation_result(self, string):
        try:
            replaced = self.replace_nth_derivative(string)
            solution = self.solve_diff_eq_from_string(replaced)
            latex_solution = pretty(solution)
            self.label_2.setText(f"{latex_solution}")
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # Center the text
        except Exception as e:
            self.label_2.setText("Hiba történt! Ellenőrizze a beírt differenciél egyenletet")
            print(e)  # Print the exception for debugging

    def replace_nth_derivative(self, eq_string):
        # Handle third-order derivatives first
        if "x'''(t)" in eq_string:
            eq_string = eq_string.replace("x'''(t)", "x(t).diff(t, t, t)")
        # Handle second-order derivatives next
        if "x''(t)" in eq_string:
            eq_string = eq_string.replace("x''(t)", "x(t).diff(t, t)")
        # Handle first-order derivatives last
        if "x'(t)" in eq_string:
            eq_string = eq_string.replace("x'(t)", "x(t).diff(t)")
        return eq_string 
        
    def solve_diff_eq_from_string(self, eq_string):
        # Splitting the equation string into left-hand side and right-hand side
        lhs_str, rhs_str = eq_string.split('=')
        
        # Parsing the variables and functions from the equation string
        t = symbols('t')
        x = Function('x')(t)
        
        # Parsing the left-hand side and right-hand side of the equation
        lhs = parse_expr(lhs_str)
        rhs = parse_expr(rhs_str)
        
        # Creating the differential equation
        diff_eq = Eq(lhs, rhs)
        
        # Solving the differential equation
        solution = dsolve(diff_eq, x)
        
        return solution

    def applyStylesheet(self, Diff_Egyenlet):

        stylesheet = """
        QMainWindow {
            background-color: #2E2E2E;
        }
        QWidget#centralwidget {
            background-color: #2E2E2E;
        }
        QLabel {
            color: #FFFFFF;
        }
        QTextEdit {
            background-color: #4E4E4E;
            color: #FFFFFF;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            background-color: #4E4E4E;
            color: #FFFFFF;
            border: 1px solid #555555;
            border-radius: 10px;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #5E5E5E;
        }
        QPushButton:pressed {
            background-color: #6E6E6E;
        }
        """
        Diff_Egyenlet.setStyleSheet(stylesheet)

    def back_to_mainwindow(self, Egyenlet, MainWindow):
        Egyenlet.close()
        MainWindow.show()

    def setupUi(self, Diff_Egyenlet, MainWindow):
        self.applyStylesheet(Diff_Egyenlet)
        Diff_Egyenlet.setObjectName("Diff_Egyenlet")
        Diff_Egyenlet.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Diff_Egyenlet)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 130, 540, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.show_diff_equation_result(self.text_edit.toPlainText().lower()))
        self.pushButton.setGeometry(QtCore.QRect(660, 60, 75, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.back_to_mainwindow(Diff_Egyenlet, MainWindow))
        self.pushButton_2.setGeometry(QtCore.QRect(720, 500, 75, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.text_edit = QTextEdit(self.centralwidget)        
        self.text_edit.setGeometry(QtCore.QRect(250, 10, 391, 101))
        self.text_edit.setObjectName("text_edit")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        Diff_Egyenlet.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Diff_Egyenlet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Diff_Egyenlet.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Diff_Egyenlet)
        self.statusbar.setObjectName("statusbar")
        Diff_Egyenlet.setStatusBar(self.statusbar)

        self.retranslateUi(Diff_Egyenlet)
        QtCore.QMetaObject.connectSlotsByName(Diff_Egyenlet)

    def retranslateUi(self, Diff_Egyenlet):
        _translate = QtCore.QCoreApplication.translate
        Diff_Egyenlet.setWindowTitle(_translate("Diff_Egyenlet", "Diff_Egyenlet"))
        self.label_2.setText(_translate("Diff_Egyenlet", "Eredmény"))
        self.pushButton.setText(_translate("Diff_Egyenlet", "Enter"))
        self.pushButton_2.setText(_translate("Egyenlet", "Vissza"))
        self.label_3.setText(_translate("Diff_Egyenlet", "Differenciál Egyenlet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.Q
