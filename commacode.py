spam = ['apples', 'bananas', 'tofu', 'cats']

def addcomma(list):
    newlist = ''
    for i in range(len(list) - 2):
        newlist += list[i] + ', '
    
    newlist += list[-2] + ' and ' + list[-1]

    return print(newlist)

addcomma(spam)