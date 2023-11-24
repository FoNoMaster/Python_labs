import matplotlib.pyplot as plt
import sympy as sp
from scipy.integrate import odeint
import numpy as np


def returns_dydt(u, t):
    dydt = -2 * u
    return dydt


x = sp.symbols('x')
y = sp.Function('y')
x_0 = 0
y_0 = sp.sqrt(2)

e = sp.Eq(y(x).diff(x), -2 * y(x))

solution = sp.dsolve(e)
print("dy(x)/dx =", e.rhs)
print("y(0) = sqrt(2)\n")
print("Решение SymPy-ем посимвольно: y(x) =", solution.rhs)
print("Найдя С1 получаем из начальных условий: y(x) =", solution.rhs.evalf(subs={sp.symbols('C1'): sp.simplify(sp.solve(solution)[0][sp.symbols('C1')]).evalf(subs={y(x): y_0, x: x_0})}))

# p1 = sp.plotting.plot(1.4142135623731*sp.exp(-2*x), (x, 0, 10))  # Решение SymPy-ем

t = np.linspace(0, 10)
r = odeint(returns_dydt, y_0, t)
arr = []
for i in range(len(t)):
    arr.append(r[i][0] - 1.4142135623731*sp.exp(-2*t[i]))

# plt.plot(t, r)  # Решение SciPy-ем

plt.plot(t, arr)  # Разность решений: SciPy - SymPy

# p1.save("SymPy_solve.png")
plt.savefig("SciPy-SymPy_solve.png")
plt.show()
