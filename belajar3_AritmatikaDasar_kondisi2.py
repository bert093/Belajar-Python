angka = int(input("Masukkan angka yang ingin ditambahkan: "))
angka_lagi = int(input("Masukkan angka lagi yang ingin ditambahkan: "))
hasil = angka + angka_lagi

formatted_hasil = f"{hasil:,}".replace(",", ".")
print (f"Hasil yang anda masukkan adalah Rp{formatted_hasil}")

#* print (f"Hasil yang anda masukkan adalah {hasil}") print normal

# if hasil >= 30:
#     print(f"Total yang anda masukkan {hasil}")
# elif hasil <= 30:
#     print(f"Hasil yang anda masukkan adalah {hasil}")