def tambah(a, b): # mendifinisikan fungsi bernama "tambah" dengan dua parameter (a dan b).
    hasil = a + b # Paramater a dan b
    pengurangan = a - b
    return hasil, pengurangan # mengembalikan nilai hasil sebagai output fungsi

hasil, pengurangan = tambah(10, 5)
print(f'Hasil dari penjumlahannya adalah {hasil}')
print(f'Hasil dari pengurangannya adalah {pengurangan}')

def sapa(nama_saya):
    print(f'Halo semuanya, nama saya adalah {nama_saya}')

sapa("Syahril")
sapa("Syahrul")