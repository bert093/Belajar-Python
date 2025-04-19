print('===List===')
list_1 = [3, 1, 4, 6, 9]
list_2 = ['budi', 'ani', 'ana']

for e in list_1:
    print('element: ', e)

for i in range(0, len(list_2)):
    print('index: ', i, 'element: ', list_2[i])

list_3 = [
    [2, 14, 6 , 2], [5, 7, 8, 2, 5], [66, 77, 88, 99, 34]
]

for row in list_3:
    for col in row:
        print(col, end ='')
        print()

print('===Konversi===')
range_1 = range(0, 15)
konv_1 = list(range_1)
print(konv_1)

range_2 = range(11, 50, 3)
konv_2 = list(range_2)
print(konv_2)

range_3 = range(100, 10, -5)
konv_3 = list(range_3)
print(konv_3)

# SLicing
print('===Slicing===')
slice_1 = list_1[0:4]
print(slice_1)

# extend
list_1.extend(list_2)
print(list_1)

list_4 = [
    'sugiono',
    'miya',
    'nayla',
    'dimas',
]

# extend slicing
list_4[len(list_4):] = list_1 # list_2 sudah digabung dengan list_1 karena menggunakan extend di atasnya.
print(list_4)


# extend operator
list_5 = [
    'walid',
    'hambali',
    'baiduri',
    'dewi',
]

list_5 = list_2+list_4
print(list_5)