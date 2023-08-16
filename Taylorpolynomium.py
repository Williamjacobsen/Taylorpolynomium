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
n = 15

f_Xo = function.replace('x', str(Xo))

tangent = math.cos(Xo) + eval(f"{sympy.diff(f_Xo)} * (x - {Xo})")
derivedFunctions = []

prevDiff = str(sympy.diff(function))
for i in range(2, n):
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




