import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import re
import numpy as np
import math

class Canvas(FigureCanvas):
    text = ""
    func = ""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)
        self.ax = self.fig.add_subplot(1, 1, 1)
        
        self.interval_x = [-10, 10]  # Initial x interval
        self.interval_y = [-10, 10]  # Initial y interval
        self.zoom_factor = 0.1  # Zoom factor
        self.df = False
        self.df_func = ""

    def f(self, x):
        return eval(self.text)

    def sec(self, x):
        return 1 / np.cos(x)

    def csc(self, x):
        return 1 / np.sin(x)

    def fact(self, x):
        if np.isscalar(x):
            return math.factorial(int(x))
        else:
            return np.array([math.factorial(int(i)) for i in x])

    def replace_numpy_funcs(self, func_str):
        replacements = {
            # log
            r"\blog\b": "np.log10",
            r"\bln\b": "np.log",
            # Inverse
            r"\barctan\b": "np.arctan",
            r"\barcsin\b": "np.arcsin",
            r"\barccos\b": "np.arccos",
            # Inverse hyperbolic
            r"\barcsinh\b": "np.arcsinh",
            r"\barccosh\b": "np.arccosh",
            r"\barctanh\b": "np.arctanh",
            # trig
            r"\bsin\b": "np.sin",
            r"\bcos\b": "np.cos",
            r"\btan\b": "np.tan",
            # hyperbolic
            r"\bsinh\b": "np.sinh",
            r"\bcosh\b": "np.cosh",
            r"\btanh\b": "np.tanh",
            # exp
            r"\bexp\(([^)]+)\)": r"np.exp(\1)",
            # abs
            r"\babs\b": "np.absolute",
            # sign(x)
            r"\bsign\b": "np.sign",
            # gyok
            r"\bsqrt\b": "np.sqrt",
            # szekánsok
            r"\bsec\b": "self.sec",
            r"\bcsc\b": "self.csc",
            r"\bpi\b": "np.pi",
            r"\bfactorial\b": "self.fact",
        }

        for pattern, replacement in replacements.items():
            func_str = re.sub(pattern, replacement, func_str)

        return func_str

    def check_for_large_jumps(self, y_vals, threshold):
        diff = np.abs(np.diff(y_vals))
        jumps = np.where(diff > threshold)[0]
        return jumps

    def clear(self):
        self.ax.clear()

    def plot_function(self, func_str, interval_x=None, interval_y=None, clear=True, C=None, df=False, df_func=""):
        if interval_x is None:
            interval_x = self.interval_x
        if interval_y is None:
            interval_y = self.interval_y
        
        self.func = func_str.replace("A", "a")
        func_str = self.replace_numpy_funcs(func_str.replace("^", "**")).replace("A", "a")
        self.text = func_str
        self.df = df
        self.df_func = df_func

        if C is not None:
            self.text = self.text.replace("C1", str(C[0]))
            self.text = self.text.replace("C2", str(C[1]))
            self.text = self.text.replace("C3", str(C[2]))

        x_vals = np.linspace(interval_x[0], interval_x[1], 10000)
        y_vals = 0

        if func_str.isdigit():
            y_vals = np.full_like(x_vals, int(func_str))
        else:
            y_vals = np.zeros_like(x_vals)
            for i, x in enumerate(x_vals):
                y_vals[i] = self.f(x)

        threshold = 10
        if "tan" in func_str or "sec" in func_str or "csc" in func_str:
            large_jumps = self.check_for_large_jumps(y_vals, threshold)
            for idx in large_jumps:
                y_vals[idx] = np.nan
            self.ax.set_ylim(interval_y[0], interval_y[1])
        else:
            pass

        if clear:
            self.ax.clear()

        self.ax.plot(x_vals, y_vals, label=f"y = {self.func}")
        self.ax.set_xlabel("x")
        self.ax.set_xlim(interval_x[0], interval_x[1])
        self.ax.set_ylim(interval_y[0], interval_y[1])
        self.ax.set_ylabel("f(x)")
        self.ax.grid(True)
        self.ax.legend()
        self.fig.savefig("plot.png")

        if df:
            self.direction_field(df_func, clear=False)

    def direction_field(self, func_str, clear=True):
        text = func_str.split("=")[1]
        func = func_str.split("=")[1]
        func = self.replace_numpy_funcs(func)

        nt, nv = 3.5, 3.5
        t = np.arange(-10, 10, nt)
        v = np.arange(-10, 10, nv)
        y, x = np.meshgrid(t, v)

        dv = eval(func)
        dt = np.ones(dv.shape)

        arrow_scale = 100  # Controls the length of the arrows
        arrow_width = 0.002  # Controls the thickness of the arrows

        if clear:
            self.ax.clear()

        self.ax.quiver(x, y, dt, dv, color="b", label=f"y'(t) = {text}", scale=arrow_scale, width=arrow_width)
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.set_ylim(self.interval_y[0], self.interval_y[1])
        self.ax.set_xlim(self.interval_x[0], self.interval_x[1])
        self.ax.set_title("Íránymező " + text)
        self.ax.legend()
        self.fig.canvas.draw()
        self.draw_idle()

    def wheelEvent(self, event):
        
        if event.angleDelta().y() > 0:  # Scroll up
            self.interval_x[0] /= (1 + self.zoom_factor)
            self.interval_x[1] /= (1 + self.zoom_factor)
            self.interval_y[0] /= (1 + self.zoom_factor)
            self.interval_y[1] /= (1 + self.zoom_factor)
        else:  # Scroll down
            self.interval_x[0] *= (1 + self.zoom_factor)
            self.interval_x[1] *= (1 + self.zoom_factor)
            self.interval_y[0] *= (1 + self.zoom_factor)
            self.interval_y[1] *= (1 + self.zoom_factor)

        self.plot_function(self.func, self.interval_x, self.interval_y, C=[1,1,1], df=self.df, df_func=self.df_func)
