from sympy import symbols, diff, simplify

# Definisikan simbol dan fungsi
x = symbols('x')
u = 3*x**2 - 5*x
v = x**3 + 2
f = u * v

# Hitung turunan dan sederhanakan
f_diff = diff(f, x)
f_diff_simplified = simplify(f_diff)

# Cetak hasil
print(f"Turunan f'(x) (tidak disederhanakan): {f_diff}")
print(f"Turunan f'(x) (disederhanakan): {f_diff_simplified}")
