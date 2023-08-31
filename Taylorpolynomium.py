import sympy
import math
import matplotlib.pyplot as plt

x = sympy.Symbol('x')

def factorial(n):
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
    return tmp

def math_func(f):
    f = f.replace('cos', 'math.cos')
    f = f.replace('sin', 'math.sin')
    return f

def exponent(num):
    if 'e' in str(num):
        size = len(str(num)) + int(str(num)[str(num).index('e') + 2:])
        num = f'{num:.{size}f}'
    return num

function = 'cos(x)'
Xo = 0
n = 10

# Pn(x) = f(Xo) + f'(Xo) / 1! * (X - Xo) + f''(Xo) / 2! * (X - Xo)**2

f_Xo = eval(math_func(str(function).replace('x', str(Xo))))
print(f"f_Xo: {f_Xo}")
prevDiff = str(sympy.diff(function))
prevDiff_Xo = prevDiff.replace('x', str(Xo))
print(f"f'(Xo): {prevDiff_Xo}")
prevDiff_Xo = eval(math_func(prevDiff_Xo))
print(f"f'(Xo): {prevDiff_Xo}")
tangent = f_Xo + prevDiff_Xo * (x - Xo)
print(f"tangent: {tangent}")

derivedFunctions = []
for i in range(2, n + 1):
    nFac = factorial(i)
    prevDiff_Xo = str(sympy.diff(prevDiff)).replace('x', str(Xo))
    prevDiff = str(sympy.diff(prevDiff))

    derivedFunctions.append(f"{exponent(eval(f'{math_func(prevDiff_Xo)}/{nFac}'))}*(x - {str(Xo)})**{i}")

finalFunc = str(tangent)
for func in derivedFunctions:
    finalFunc += f" + {func}"
print(finalFunc)

xAxisGraph = []
yAxisGraph = []
for x in range(-80, 80, 1):
    x = x / 10
    yAxisGraph.append(eval(math_func(function)))
    xAxisGraph.append(x)

plt.plot(xAxisGraph, yAxisGraph, color='blue')

xAxisTaylor = []
yAxisTaylor = []
for x in range(-80, 80, 1):
    x = x / 10

    if eval(finalFunc) > max(yAxisGraph) * 2:
        continue
    elif eval(finalFunc) < min(yAxisGraph) * 2:
        continue

    yAxisTaylor.append(eval(finalFunc))
    xAxisTaylor.append(x)

plt.plot(xAxisTaylor, yAxisTaylor, color='green') # linestyle=(0, (5, 5)), linewidth=2
plt.show()

if __name__ == '__main__':
    pass


