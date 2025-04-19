text="Hello kelas D"
print(text)

multiline="""ini text
multiline format string
saja yang otomatis membuat
garis baru"""
print(multiline)

print("===========Pembatas===========")
# \n = membuat baris baru
# \t = membuat jarak
mursyid = "sugiono"
budak = "dewi"

print("Nama\t\t|Usia\t|Kelamin")
print(f"{mursyid}\t\t|34\t|laki-laki")
print(f"{budak}\t\t|23\t|perempuan")
print("test\n|23\n|saja")

print("===========Definisi===========")
def nama_lengkap(): # tanpa parameter dan variabel
    print("Sugiono")
nama_lengkap()

print("======Luas Lingkaran======")
def luas_lingkaran(r): # r = parameter
    luas = 3.14*r*r
    print(luas)
luas_lingkaran(4) # butuh angka

print("======Luas Persegi======")
def luas_persegi(sisi:int , pesan:str):
    luas = sisi*sisi
    print(pesan, luas)
luas_persegi(6, "luas:") # int, str dari definisi

print("======Luas Segitiga======")
def luas_segitiga(alas:int, tinggi:float)-> float:
    return 0.5*alas*tinggi
print(luas_segitiga(3,55))
luas_segitiga(4, 5) # alas, tinggi: int dan float