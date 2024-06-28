import numpy as np
import matplotlib.pyplot as plt

def direction_field(f):

    nt, nv = 0.5, 0.5
    t = np.arange(-4, 4, nt)
    v = np.arange(-4, 4, nv)

    # rectangular grid with points
    x, t = np.meshgrid(t, v)

    # derivative
    func = f.split("=")[1]
    print(func)
    dv = eval(func)
    dt = np.ones(dv.shape)

    plt.quiver(x, t, dt, dv, color='black')
    plt.title('Direction Field for ' + func)
    plt.show()

direction_field("x'(t)=np.sin(t)")