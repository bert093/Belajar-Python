import array

angka = array.array('i', [50, 90, 150])
for nilai in angka:
    print(nilai)

kalimat = array.array('u', ['h', 'e', 'l', 'l', 'o']) # unicode di versi 3.16 akan dihapus
for huruf in kalimat:
    print(huruf)