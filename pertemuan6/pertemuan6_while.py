perulangan = 1
while (perulangan < 10):
    print("Perulangan ke:", perulangan)
    perulangan += 2
print("perulangan selesai")

# perintah for

perulangan = 1, 6, 16, 21, 31
for x in perulangan:
    print(x + 4)

# perulangan dengan besaran (nestedloop)
# PERULANGAN FOR

mystop = int(input("jumlah stop: "))

# for i in range(2):
#     for j in range(6, 20, 3):
#         print("nilai i =", i , "nilai j =", j)
#     print() # memberi garis baru ketika setiap perulangan i dan j selesai

# for u in range(5, 10):
#     print("Nilai u =", u)

# for n in range(10):
#     print(n)
for m in range(2):
    for n in range(3, mystop, 2):
        print(f'nilai m = {m} nilai n= {n}')
    print()