#represent a class for the number sorter
class EvodSort:
    """"Arrange even and odd numbers from the numbers file in ascending order and write them to their respective files"""
    def __init__(self):
        #initializes empty list to hold even and odd numbers
        self.even = []
        self.odd = []

        #open the files with its method
        numbers_file = open("numbers.txt", "r")
        even_file = open("even.txt", "w")
        odd_file = open("odd.txt", "w")

        #loop through the lines in the file
        for line in numbers_file:
            #loop through the numbers
            for num in line.split():
                num = int(num)
                #assess if the number is even or odd
                if num % 2 == 0:
                    #add the even numbers to the even list
                    self.even.append(num)
                else:
                    #add the odd numbers to the odd list
                    self.odd.append(num)
 
        #sort even and odd numbers in ascending order
        self.even.sort()
        self.odd.sort()

        #add a header and border to even and odd files
        #for even, write the header decorations
        even_file.write("*" * 20 + "\n")
        even_file.write("*   EVEN NUMBERS   *\n")
        even_file.write("*" * 20 + "\n")

        #write the even numbers to the even_file with the decor
        for num in self.even:
            even_num = str(num)
            padding = (20 -len(even_num) - 2) // 2
            even_file.write("*" + " " * padding + even_num + " " * padding + "*" + "\n")
        even_file.write("*" * 20)

        #for odd, write the header decorations 
        odd_file.write("*" * 20 + "\n")
        odd_file.write("*   ODD NUMBERS   *\n")
        odd_file.write("*" * 20 + "\n")

        #write odd numbers to the odd_file with the decor
        for num in self.odd:
            odd_num = str(num)
            padding = (20 -len(odd_num) - 2) // 2
            odd_file.write("*" + " " * padding + odd_num + " " * padding + "*" + "\n")
        odd_file.write("*" * 20)  

        #close all the files
        numbers_file.close()
        even_file.close()
        odd_file.close()

EvodSort()

