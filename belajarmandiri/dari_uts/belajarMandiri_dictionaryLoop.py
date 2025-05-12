myDictionary = {
    'Christopher': [30, 'Top'],
    'Luna': [21, 'Lin'],
    'Meow': [22, 'Kucinng',]
}
for nama, data in myDictionary.items():
    umur, tambahan = data # unpack list/tupple di dalam loop
    print(f'Nama: {nama}, Umur: {umur}, Info Tambahan: {tambahan}')