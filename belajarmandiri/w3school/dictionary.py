thisdict = {
    'name': 'Ford',
    'car': 'Mustang',
    'have': 'me',
}
print(thisdict)

newdict = {
    'brand': 'Google',
    'employees': 'Google Work',
    'search': 'Google Search Engine'
}
print(newdict["brand"]) #* This is index value
x = newdict.get('employees') #* Accessing items with x variable
# x = newdict['employees'] # Or like this
y = newdict.keys() # get keys
print(x)
print(y) #* print all keys

# change the values
newdict['employees'] = 'yellow'
print(newdict)

# check if the key exist
print('==========Check the key exist==========')
if 'brand' in newdict:
    print('The brand key are exist!')
if 'employees' in newdict:
    print('The employees key are exist!')
if 'search' in newdict:
    print('The search key are exist!')