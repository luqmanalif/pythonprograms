integer = int(input('enter an integer'))

if pwr < 6 and pwr > 0:
    if root**pwr == integer:
        print(root)
        print(pwr)
else:
    print('Theres no such pair of integer')
