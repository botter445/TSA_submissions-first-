import math
#palindrome detector
"""
This converts the users input to a list that is filtered
to remove all punctuation and get rid of punctuation.
we begin at the middle letter of the list then we move
outwards from the middle, checking them with the other letter exactly the same 
distance from the middle letter. If at any point the letters are not equal 
we print a failure and exit.
this algorithm works in n/2 iterations for a length n string
though it does do 2 data requests for each iteration
"""
real_word = input("Please provide a word to be checked: ")
word = list(filter(lambda x: x not in " ?.!", [char.lower() for char in real_word]))
length = len(word)/2
for i in range(math.floor(length)):
    if not (word[math.floor(length)+i]==word[math.floor(length)-i]):
        print("Results: " + real_word + " is not a palindrome.")
        exit()
print("Results: " + real_word + " is a palindrome.")
