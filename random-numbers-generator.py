import random

#create empty list to store the numbers
numbers = []
#generate 20 integers from 1-100
for x in range(20):
    #the integers will append to the list
    numbers.append(random.randint(1, 100))

#to store the numbers to our number.txt file -
#open a file in write mode
file = open("numbers.txt", "w")

#for loop the number from the list to the file
for num in numbers:
    #turn int to str and separate the numbers in each line
    file.write(str(num) + "\n")

#close the file
file.close()