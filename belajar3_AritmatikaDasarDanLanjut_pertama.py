a = 12
b = 9
hasil = a + b # pertambahan
hasil2 = a - b # pengurangan
hasil3 = a * b # perkalian
hasil4 = a / b # pembagian 
hasil5 = a // b # menghasilkan hasil pembagian dalam bilangan bulat
hasil6 = a % b # hasil sisa pembagian
hasil7 = a ** b
print(f'hasil 1 adalah {hasil}')
print(f'hasil 2 adalah {hasil2}')
print(f'hasil 3 adalah {hasil3}')
print(f'hasil 4 adalah {hasil4}')
print(f'hasil 5 adalah {hasil5}')
print(f'hasil 6 adalah {hasil6}')
print(f'hasil 7 adalah {hasil7}')

sama_dengan = (a == b) # memeriksa dua nilai apakah sama atau tidak
tidak_samadengan = (a != b) # memeriksa dua nilai apakah a tidak sama dengan b
lebih_besar = (a > b) # memeriksa dua nilai apakah a lebih besar daripada b
apakah = (hasil >= 18 and hasil<= 65) # memeriksa apakah 'hasil' nilainya >= 18 dan <= 65

print(f'{sama_dengan}. karena nilai 12 tidak sama dengan 9 (false/salah)')
print(f'{tidak_samadengan}. karena nilai 12 tidak sama dengan 9 (benar/true)')
print(f'{lebih_besar}. karena nilai 12 lebih besar dari 9 (benar/true)')
print(f'{apakah}. karena 12+9 = 21 sehingga benar dari rumusnya, yaitu >= 18 and <= 65')