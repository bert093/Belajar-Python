import array
# a = 2
# b = 4
# c = a + b
# print("hasil a + b")

angka = array.array('i',[1, 2, 3]) # tipe data integer
kalimat = ['Halo', 'dimas', 'test array dalam string!']

angka.append(50)
angka.remove(1)
for array in angka:
    print(array)

kalimat.append('test')
kalimat.remove('dimas')
print(kalimat)