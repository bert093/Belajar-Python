myDictionary = {
    'Christopher': [30, 'Top', 'Manusia'], #* Multiple Values
    'Luna': [20, 'Lin', 'Manusia'],
    'Meow': [21, 'Kucing', 'Manusia']
}

for nama, (umur, tambahan, spesies) in myDictionary.items():
    print(f'Nama: {nama} Umur: {umur} Tambahan: {tambahan} Spesies: {spesies}')