ipk = int (input("Masukkan nilai IPK anda: "))

if ipk >= 81:
    print('Nilai A')
# elif ipk >= 80:
#     print("Hasil IPK anda adalah B+")
elif ipk >= 71:
    print('Nilai B+')
elif ipk >= 61:
    print('Nilai B')
elif ipk >= 51:
    print('Nilai C+')
elif ipk >= 41:
    print("Nilai C")
elif ipk >= 31:
    print('Nilai D')
else:
    print("Tidak lulus")