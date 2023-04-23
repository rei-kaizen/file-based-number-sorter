#represent a class for the number sorter
class EvodSort:
    """Initialize instances for the class and create empty lists to hold for even and odd numbers"""
    def __init__(self):
        self.even = []
        self.odd = []

        #open the files
        numbers_file = open("numbers.txt", "w")
        even_file = open("even.txt", "w")
        odd_file = open("odd.txt", "w")

        numbers_file.close()
        even_file.close()
        odd_file.close()

#loop through the line in the file
    def evod_filter(self, numbers_file):
        """Filter the odd and even number in numbers_file"""
        for line in numbers_file:
            #loop through the numbers
            for num in line.split():
                num = int(num)
                #assess if even or odd
                if num % 2 == 0:
                    #add the numbers to the even list
                    self.even.append(num)
                else:
                    #add the numbers to the odd list
                    self.odd.append(num)
##if even, add the numbers to the even list then write the numbers to the  even file
##else, add the numbers to the odd list  write the numbers to the odd file

EvodSort()

