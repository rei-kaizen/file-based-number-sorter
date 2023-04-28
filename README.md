# file-based-number-sorter
The is program generates 20 random numbers between 1 and 100, store them in a file named numbers.txt, and then sort the even and odd numbers into separate files named `even.txt` and `odd.txt` respectively.

## The program consists of two parts:

### Generating Random Numbers and Saving to File
The first part generates a list of 20 random integers between 1 and 100 and saves them to a file named "numbers.txt". 
This is accomplished using the built-in Python module `random`. 
The purpose of this part of the program is to create a source file of random numbers that can be used for further processing.

### Sorting Even and Odd Numbers and Saving to Separate Files
The second part of the program is a class called `EvodSort` that reads the numbers from the "numbers.txt" file.
Then separates them into even and odd numbers, sorts them in ascending order, and saves them to two separate files named "even.txt" and "odd.txt" respectively. 
The purpose of this part of the program is to arrange the numbers in a way that is useful for further analysis or processing.

## 📄 Documentation 
<details><summary><h3> 🤔 Usage </h3></summary>

-----

1. Download or copy and paste the code into a Python file named numbersort.py.
2. Run the program in the terminal or command prompt by typing python numbersort.py.
3. Check the directory for the files numbers.txt, even.txt, and odd.txt. These files will contain the generated numbers and the sorted even and odd numbers respectively.

or

1. Fork this repository 
2. Once the repository has been forked, you can clone the repository to your local machine using the `git clone` command followed by the repository URL.
3. Once the repository is cloned, navigate to the directory of the cloned repository using the `cd` command.
4. Now you can work with the files in the cloned repository.
5. If you want to keep your fork in sync with this repository, you can use the `git fetch` and `git merge` commands to pull in changes and merge them into your local copy.

**Reminders:**
> The program generates random numbers, so the results will be different each time you run the program.
 The program creates a new file with random numbers.
 If you run the program multiple times, the previous file will be overwritten.
 The program requires two parts to work, and it's essential to run both parts in the correct order.

</details>

<details><summary><h3> 🔰 Additional information </h3></summary>

-----

**Program 1: Random Numbers Generator**
<br>

-This program uses the `random` module to generate 20 random integers between 1 and 100.<br>
-The generated numbers are stored in a list, which is then written to a file named `numbers.txt`.<br> 
-Each number is written on a separate line.<br>
<br>

**Program 2: Even and Odd numbers Sorter**
<br>

-This program uses a class called `EvodSort` to sort the even and odd numbers from the `numbers.tx` file into separate lists. <br>
-The even and odd lists are then sorted in ascending order using the `sort()` method.<br>
-The sorted even and odd numbers are then written to their respective files, `even.txt` and `odd.txt`. <br>
-Each file contains a header with decorations, indicating whether it contains even or odd numbers. <br>
-Each number is also separated by a line.<br>

</details>

<details><summary><h3> 💡 Purpose </h3></summary>

-----

The two parts of the program work together to generate random numbers and sort them into even and odd numbers. Hence, this is useful for generating random data and sorting it for further processing.

</details>

