import numpy


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


if __name__ == "__main__":
    x = numpy.array([1, 2, 3])
    y = f(x)
    middle = solve_equation(f, left=1, right=3)
    print(middle)
    print(f(middle))