def my_function(fname):
    print(fname + "test")

my_function("emila")
my_function("Tobila")
my_function("Nama")

# number argument
print("====== Number Argument ======")
def my_function2(firstname, lastname):
    print(firstname + " " + lastname)
my_function2("dimas", "budi")

#- * args
print("====== * args ======")
def my_function3(*kids):
    print("test saja gunakan * args index 1: " + kids[1])

my_function3("Luci", "Lina", "Dimas") # index

# keyword argument

print("====== Keyword Argument ======")
def my_function4(child1, child2, child3):
    print("test menggunakan keyword argument: " + child3)

my_function4(child1 = "test", child2 = "test2", child3 = "test3")

# Default Parameter Value
def my_function5(country = "Indonesia"):
    print("Saya dari " + country)

my_function5("Malaysia")
my_function5("Singapura")
my_function5() # memanggil default parameternya sendiri (function5)
my_function5("Surabaya")