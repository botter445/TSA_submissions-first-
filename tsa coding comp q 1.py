
temp = input('What tempature')
not_solved = True
temptype = ''
tempnum = ''
#speratre numbers and letters
for characters in temp:
    if characters.isalpha():
        temptype += characters
    if characters.isdigit():
        tempnum += characters
tempnum = int(tempnum)
#main loop so it can keep trying untill solved.
while not_solved:
    next = input('Conversion Options: \n 1. Convert to Celsius \n 2. Convert to Fahrenheit \n 3. Convert to Kevlin')
    if temptype == 'K':
        if next == '1' or '2':
            tempnum = tempnum - 273.15
            if next == '1':
                print('converted temperature' + str(tempnum) + ' Celsius')
            elif next == '2':
                tempnum = tempnum*1.8  + 32
                print('converted temperature' + str(tempnum) + ' Fahrenheit')
            not_solved = False
        elif next == '3':
            print('you already have it in Kelvin')
        else:
            pass

    if temptype == 'C':
        if next == '2' or '3':
            if next == '3':
                tempnum = tempnum + 273.15
                print('converted temperature' + str(tempnum) + ' Kelvin')
            elif next == '2':
                tempnum = tempnum * 1.8 + 32
                print('converted temperature' + str(tempnum) + ' Fahrenheit')
            not_solved = False
        elif next == '1':
            print('It is already in Celsius')
        else:
            pass
    if temptype == 'F':
        if next == '3' or '1':
            tempnum = (tempnum - 32) * (5/9)
            if next == '3':
                tempnum = tempnum + 273.15
                print('converted temperature' + str(tempnum) + ' Kelvin')
            elif next == '1':
                print('converted temperature' + str(tempnum) + ' Celsius')
            not_solved = False
        elif next == '2':
            print('It is already in Fahrenheit')
        else:
            pass

