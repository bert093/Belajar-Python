ipk = int (input("Masukkan nilai IPK anda: "))

if ipk >= 81:
    print('Hasil IPK anda adalah A')
elif ipk >= 80:
    print("Hasil IPK anda adalah B+")
elif ipk >= 71:
    print('Hasil IPK anda adalah B')
elif ipk >= 61:
    print('Hasil IPK anda adalah C')
elif ipk >= 51:
    print('Hasil IPK anda adalah D')
elif ipk >= 41:
    print("Hasil IPK anda adalah E")
elif ipk >= 31:
    print('Hasil IPK anda adalah F')
else:
    print("Hasil IPK anda adalah F")