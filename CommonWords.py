first = input('Enter the first sentence: ')
second = input('Enter the second sentence:')
first_list = list(filter(lambda x: x not in ",./;'\[]-=!@#$%^&*()_+-=`~|",[char for char in first]))
first = []
b=''
for x in first_list:
    if x == " ":
        first.append(b)
        b=''
    else:
        b+=x.lower()
first.append(b)
second_list = list(filter(lambda x: x not in ",./;'\[]-=!@#$%^&*()_+-=`~|",[char for char in second]))
second = []
b=''
for x in second_list:
    if x == " ":
        second.append(b)
        b=''
    else:
        b+=x.lower()
second.append(b)
both = []
unique = []
num_of_vowels = 0
for onewords in first:
    for words in second:
        if onewords == words:
            both.append(onewords)
unique.extend([x for x in first if x not in both])
unique.extend([x for x in second if x not in both])

for char in first:
    for x in char:
        if x in "aeiou":
            num_of_vowels+=1
for char in second:
    for x in char:
        if x in "aeiou":
            num_of_vowels+=1

c = ''
for b in range(len(unique)):
    if b!=len(unique)-1:
        c += unique[b]+', '
    else:
        c+=unique[b]
both = list(set(both))
unique = list(set(unique))
the_list = []
for x in both:
    instance_count = 0
    for t in first:
        if x ==t:
            instance_count +=1
    for t in second:
        if x ==t :
            instance_count +=1
    the_list.append(instance_count)
new_string = ''
for i in range(len(both)):
    if i == len(both)-1:
        new_string += " " + str(both[i]) + " - " + str(the_list[i])
        break
    new_string += " " + str(both[i]) + " - " + str(the_list[i])+ ','
print('Words in both sentences:'+ new_string)
print('Unique words: '+str(c))
print('Number of vowels: '+ str(num_of_vowels))
