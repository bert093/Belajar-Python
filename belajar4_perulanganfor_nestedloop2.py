jmh = int(input("jumlah binatang: "))

for i in range(jmh):
    for j in range(0, jmh -i):
        print("*", end="")
        print()