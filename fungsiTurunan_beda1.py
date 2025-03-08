from sympy import symbols, diff

# Definisikan simbol dan fungsi
x = symbols('x')
u = 3*x**2 - 5*x
v = x**3 + 2
f = u * v

# Hitung turunan
f_diff = diff(f, x)

# Cetak hasil
print(f"Fungsi f(x): {f}")
print(f"Turunan f'(x): {f_diff}")