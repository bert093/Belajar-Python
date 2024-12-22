from sympy import *
x, y, z = symbols('x y z')

#* fungsi 1
expr1 = x** 3 + 2*x**2 -5 # x pangkat 3 + 2x pangkat 2 -5
expr1_diff = Derivative(expr1, x).doit() #* membuat objek turunan dari variable expr1 terhadap variabel x (hanya mendefinisikan, belum dihitung)

#* fungsi 2
expr2= y**2 * x + 3*y
expr2_diff = Derivative(expr2, y).doit()

#* fungsi 3
expr3 = z**4 + 2*z**3 - z + 7
expr3_diff = Derivative(expr3, z).doit()

#* Cetak hasilnya
print(f"Fungsi 1: {expr1}")
print(f"Fungsi turunan 1 terhadap x: {expr1_diff}") #* diff dalam konteks ini adalah konvensi penamaan untuk menunjukkan bahwa variabel tersebut menyimpan hasil turunan suatu fungsi

print(f"Fungsi 2: {expr2}")
print(f"Fungsi turunan 2 terhadap y {expr2_diff}")

print(f"Fungsi 3: {expr3}")
print(f"Fungsi turunan 3 terhadap z {expr3_diff}")