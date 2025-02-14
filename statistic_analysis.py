"""
It is not explicitly stated if the code should except 2 digit numbers

"""
real_dataset = input("Please enter the dataset: ")
dataset = list(filter(lambda x: x not in " ,", [char for char in real_dataset]))
dataset = [int(x) for x in dataset]
print(dataset)
no_duplicates = list(set(dataset))
frequency = [0 for x in range(len(no_duplicates))]
length = len(dataset)
mean = 0 #this is another word for average
for i in range(length):
    mean += dataset[i]
    frequency[no_duplicates.index(dataset[i])] += 1
mean = round(mean/length,2)
print("Average of the dataset: " + str(mean))
for i in range(len(no_duplicates)):
    print(str(no_duplicates[i]) + " appeared " + str(frequency[i]) + " times within the dataset")




