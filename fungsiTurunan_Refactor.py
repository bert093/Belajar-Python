from sympy import symbols, diff

# Mendefinisikan simbol
x, y = symbols('x y')

# Ekspresi matematika
expr = x**2 + 2*y + y**3
print(f"Expression: {expr}")

# Turunan ekspresi terhadap x
expr_diff = diff(expr, x)
expr_diff_y = diff(expr, y)
print(f"Derivative of expression with respect to x: {expr_diff}")
print(expr_diff_y)