integer = int(input('Enter a number:'))
what_to_print = []
for ints in range(integer):
    if (ints+1)%3 == 0 and (ints+1)%5 == 0:
        what_to_print.append('FizzBuzz')
    else:
        if (ints+1)%3 == 0:
            what_to_print.append('Fizz')
        elif (ints+1)%5 == 0:
            what_to_print.append('Buzz')
        else:
            what_to_print.append(str(ints+1))
c = ''
for b in what_to_print:
    c += b+', '
print(c)