import numpy
import matplotlib.pyplot as plt
from config_file import *

def f(x): 
    return x**2 - 8 * numpy.log(x)

def solve_equation(f, left, right, precision):
    while right - left >= precision:
        middle = (left + right) / 2
        if f(middle) == 0:
            break

        elif f(left) * f(middle) < 0:
            right = middle
        
        elif f(right) * f(middle) < 0:
            left = middle
    return middle

def plot_function(f, start, end, step):
    x = numpy.arange(start, end, step)
    y = f(x)
    plt.figure(figsize=(LENGTH, HIGHT)) # 15 en lageur et 6 en hauteur
    plt.plot(x, y)
    plt.show()



if __name__ == "__main__":
    #x = numpy.array([1, 2, 3])
    #y = f(x)
    plot_function(f, start=0.01, end=5, step=0.01)
    """middle = solve_equation(f, left=1, right=3)
    print(middle)
    print(f(middle))"""