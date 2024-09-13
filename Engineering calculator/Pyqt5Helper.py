from PyQt5.QtWidgets import QMainWindow, QComboBox
from PyQt5.QtGui import QIcon
from GUI_Calculus_window import Ui_Calculus
from GUI_Equality_window import Ui_Equation
from GUI_Differential_Equation_window import Ui_Differential_Equation
from GUI_Probability_and_statistics_window import Ui_Probability_and_statistics
from GUI_Programmer_calculator_window import Ui_Programmer_calculator
from PyQt5.QtCore import pyqtSlot


class Pyqt5Helper:
    def __init__(self, icon_path):
        self.icon_path = icon_path

    def create_combobox(self, MainWindow):
        comboBox = QComboBox()
        comboBox.addItems(
            [
                "Select one:",
                "Basic",
                "Calculus",
                "Equations",
                "Differential Calculation",
                "Probability and Statistics",
                "Programmer Calculator",
            ]
        )
        # Connect the currentIndexChanged signal to the generate_window method
        comboBox.currentIndexChanged.connect(
            lambda: self.generate_window(comboBox, MainWindow)
        )
        return comboBox

    @pyqtSlot()  # Ensures the method can be used as a slot
    def generate_window(self, comboBox, MainWindow):
        index = comboBox.currentIndex()
        window_type = comboBox.itemText(index)

        if window_type == "Calculus":
            self.generate_calculus(MainWindow)
            MainWindow.hide()
        elif window_type == "Equations":
            self.generate_equation(MainWindow)
            MainWindow.hide()
        elif window_type == "Differential Calculation":
            self.generate_diff_equation(MainWindow)
            MainWindow.hide()
        elif window_type == "Probability and Statistics":
            self.generate_prob_and_stat(MainWindow)
            MainWindow.hide()
        elif window_type == "Programmer Calculator":
            self.generate_programmer_calculator(MainWindow)
            MainWindow.hide()

    def generate_calculus(self, MainWindow):
        self.window = QMainWindow()
        self.ui = Ui_Calculus()
        self.ui.setupUi(self.window, MainWindow)
        self.window.setWindowIcon(QIcon(self.icon_path))
        self.window.show()

    def generate_equation(self, MainWindow):
        self.window = QMainWindow()
        self.ui = Ui_Equation()
        self.ui.setupUi(self.window, MainWindow)
        self.window.setWindowIcon(QIcon(self.icon_path))
        self.window.show()

    def generate_diff_equation(self, MainWindow):
        self.window = QMainWindow()
        self.ui = Ui_Differential_Equation()
        self.ui.setupUi(self.window, MainWindow)
        self.window.setWindowIcon(QIcon(self.icon_path))
        self.window.show()

    def generate_prob_and_stat(self, MainWindow):
        self.window = QMainWindow()
        self.ui = Ui_Probability_and_statistics()
        self.ui.setupUi(self.window, MainWindow)
        self.window.setWindowIcon(QIcon(self.icon_path))
        self.window.show()

    def generate_programmer_calculator(self, MainWindow):
        self.window = QMainWindow()
        self.ui = Ui_Programmer_calculator()
        self.ui.setupUi(self.window, MainWindow)
        self.window.setWindowIcon(QIcon(self.icon_path))
        self.window.show()
