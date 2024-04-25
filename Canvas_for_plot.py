from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import re
import numpy as np

class Canvas(FigureCanvas):

    text = ""
    func = ""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.setParent(parent)
        self.ax = self.fig.add_subplot(1, 1, 1)

    def f(self, x):
        return eval(self.text)
    
    def sec(self, x):
        return (1/np.cos(x))
    def csc(self, x):
        return (1/np.sin(x))

    def replace_numpy_funcs(self, func_str):
        replacements = {
            # log
            r'\blog\b': 'np.log10',
            r'\bln\b': 'np.log',
            # Inverse
            r'\barctan\b': 'np.arctan',
            r'\barcsin\b': 'np.arcsin',
            r'\barccos\b': 'np.arccos',
            # Inverse hyperbolic
            r'\barcsinh\b': 'np.arcsinh',
            r'\barccosh\b': 'np.arccosh',
            r'\barctanh\b': 'np.arctanh',
            # trig
            r'\bsin\b': 'np.sin',
            r'\bcos\b': 'np.cos',
            r'\btan\b': 'np.tan',
            # hyperbolic
            r'\bsinh\b': 'np.sinh',
            r'\bcosh\b': 'np.cosh',
            r'\btanh\b': 'np.tanh',
            # exp
            r'\bexp\b': 'np.exp',
            # abs
            r'\babs\b': 'np.absolute',
            # sign(x)
            r'\bsign\b': 'np.sign',
            #gyok
            r'\bsqrt\b': 'np.sqrt',
            #szekánsok
            r'\bsec\b': 'self.sec',
            r'\bcsc\b': 'self.csc'
        }

        for pattern, replacement in replacements.items():
            func_str = re.sub(pattern, replacement, func_str)

        return func_str

    def check_for_large_jumps(self, y_vals, threshold):
        diff = np.abs(np.diff(y_vals))
        jumps = np.where(diff > threshold)[0]
        return jumps

    def plot_function(self, func_str, interval):
        self.ax.clear()

        self.func = func_str.replace("A", "a")
        func_str = self.replace_numpy_funcs(func_str.replace("^", "**")).replace("A", "a")
        self.text = func_str
        print("self: " + self.text)
        print(interval)

        x_vals = np.linspace(interval[0], interval[1], 10000)

        if func_str.isdigit():  # Handle static function like 4
            y_vals = np.full_like(x_vals, int(func_str))
        else:
            y_vals = self.f(x_vals)

        threshold = 10
        if "tan" in func_str or "sec" in func_str or "csc" in func_str:
            large_jumps = self.check_for_large_jumps(y_vals, threshold)
            for idx in large_jumps:
                y_vals[idx] = np.nan
            self.ax.set_ylim(-10, 10)
        else:
            pass  # You can add specific handling for other types of functions if needed

        self.ax.plot(x_vals, y_vals, label=f'y = {self.func}')
        self.ax.set_xlabel('x') 
        self.ax.set_xlim(interval[0], interval[1])
        self.ax.set_ylabel('f(x)') 
        self.ax.grid(True) 
        self.ax.legend()  
        self.fig.savefig('plot.png')