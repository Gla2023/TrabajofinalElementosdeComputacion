import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from matplotlib.patches import Polygon

def funciones(oferta, demanda):
    """ 
    Input: Supply and Demand, type X variable functions
    Output: Variable x, type variable
    """
    x = sp.Symbol('x')
    return x

def equilibrio_func(x):
    """
    Parameters:
    x : TYPE variable
        DESCRIPTION: generated by "funciones"
    
    Returns:
    -------
    float
        DESCRIPTION. Market equilibrium price
    """
    return oferta.subs('x', x) - demanda.subs('x', x)

oferta_str = input("Ingrese la fórmula de la función de oferta (m*x+b or ax*x+b*x+c): ")
demanda_str = input("Ingrese la fómula de la función de demanda ( m*x+b or ax*x+b*x+c): ")

x = sp.Symbol('x')
oferta = sp.sympify(oferta_str)
demanda = sp.sympify(demanda_str)

equilibrio = brentq(equilibrio_func, 0, 1000)

print(f"El precio de equilibrio es {equilibrio}")

def integral(f, a, b):
    """
    Parameters
    ----------
    f : TYPE Function
        DESCRIPTION. Supply and demand
    a, b : TYPE float
        DESCRIPTION. Integration Extremes
   Returns
    -------
    integral : TYPE float
        DESCRIPTION. Area under the curve
    """
    x = sp.Symbol('x')
    integral = sp.integrate(f, (x, a, b))
    return integral

exceso_demanda = abs(integral(demanda, 0, equilibrio) - (equilibrio * demanda.subs('x', equilibrio)))
print(f"El exceso de demanda es {exceso_demanda}")

exceso_oferta = abs((equilibrio * oferta.subs('x', equilibrio)) - integral(oferta, 0, equilibrio))
print(f"El exceso de oferta es {exceso_oferta}")

x_values = np.linspace(0, equilibrio * 2, 400)
oferta_values = [oferta.subs('x', val) for val in x_values]
demanda_values = [demanda.subs('x', val) for val in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, oferta_values, label='Oferta', color='blue')
ax.plot(x_values, demanda_values, label='Demanda', color='red')
ax.scatter(equilibrio, oferta.subs('x', equilibrio), color='green', label='Equilibrio')

polygon_points = [(x_val, demanda.subs('x', x_val)) for x_val in x_values if x_val <= equilibrio]
polygon_points.append((equilibrio, oferta.subs('x', equilibrio)))
polygon = Polygon(polygon_points, closed=True, alpha=0.2, facecolor='orange', edgecolor='none')
ax.add_patch(polygon)

polygon_points = [(x_val, oferta.subs('x', x_val)) for x_val in x_values if x_val <= equilibrio]
polygon_points.append((equilibrio, demanda.subs('x', equilibrio)))
polygon = Polygon(polygon_points, closed=True, alpha=0.2, facecolor='purple', edgecolor='none')
ax.add_patch(polygon)

ax.set_xlabel('Cantidad')
ax.set_ylabel('Precio')
ax.legend()
ax.grid()
plt.show()


