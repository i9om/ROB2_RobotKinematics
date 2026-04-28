# Solutions to exercise 1.2 on Forward Kinematics
# Using pythons symbolic toolbox: Sympy

import sympy as sm

# Define TDH-funktionen
def TDH(alpha: object, a: object, d: object, theta: object) -> object:
    return sm.Matrix([
        [sm.cos(theta), -sm.sin(theta), 0, a],
        [sm.sin(theta) * sm.cos(alpha), sm.cos(theta) * sm.cos(alpha), -sm.sin(alpha), -d * sm.sin(alpha)],
        [sm.sin(theta) * sm.sin(alpha), sm.cos(theta) * sm.sin(alpha), sm.cos(alpha), d * sm.cos(alpha)],
        [0, 0, 0, 1]
    ])

theta1, d2, theta3, L1 = sm.symbols('theta1 d2 theta3 L1')

# compute transformation matrices

T01 = TDH(0,       0,  0,  theta1)
T12 = TDH(sm.pi/2, L1, d2, 0)
T23 = TDH(sm.pi/2, 0,  0,  theta3)

# Compute and simplify
T03 = sm.simplify(T01 * T12 * T23)

# Print resultat
# Configure pprint for long lines

sm.init_printing(use_unicode=True, wrap_line=False)

sm.pprint((T03))