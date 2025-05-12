x = 'print(55)'
eval(x)

# melakukan ekpresi matematika dari string
expression = "5 * (3 +2)" # 5 x 5
result = eval(expression)
print(result)

# Mengevaluasi ekspresi dalam konsteks variable tertentu
x = 2
y = 10
result = eval("x * y + 2")
print(result)