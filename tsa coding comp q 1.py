
temp = input('What tempature')
print(temp)
not_solved = True
temptype = ''
tempnum = ''
for characters in temp:
    if characters.isalpha():
        temptype += characters
    if characters.isdigit():
        tempnum += characters
tempnum = int(tempnum)
print(tempnum)
print(temptype)
while not_solved:
    if temptype == 'K':
        next = input('what would you like to convert to C or F')
        if next == 'C' or 'F':
            tempnum = tempnum - 273.15
            if next == 'C':
                print('new temp is ' + str(tempnum) + 'C')
            elif next == 'F':
                tempnum = tempnum*1.8  + 32
                print('new temp is ' + str(tempnum) + 'F')
            not_solved = False
        else:
            next = input('Please put in C for Celsius or F for Fahrenheit capital')

    if temptype == 'C':
        next = input('what would you like to convert to K or F')
        if next == 'K' or 'F':
            if next == 'K':
                tempnum = tempnum + 273.15
                print('new temp is ' + str(tempnum) + 'K')
            elif next == 'F':
                tempnum = tempnum * 1.8 + 32
                print('new temp is ' + str(tempnum) + 'F')
            not_solved = False
        else:
            next = input('Please put in K for Kelvin or F for Fahrenheit capital')
    if temptype == 'F':
        next = input('what would you like to convert to K or C')
        if next == 'K' or 'C':
            tempnum = (tempnum - 32) * (5/9)
            if next == 'K':
                tempnum = tempnum + 273.15
                print('new temp is ' + str(tempnum) + 'K')
            elif next == 'C':
                print('new temp is ' + str(tempnum) + 'C')
            not_solved = False
        else:
            next = input('Please put in K for Kelvin or C for Celsius capital')

