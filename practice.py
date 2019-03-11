# Import requirements
import math
import string

# =================================================================
# Function Question Index:
# =================================================================
# Generally questions with notes are fully explained questions.
# Run code in terminal with python practice.py

# Jose Portilla Python Bootcamp
# Functions and Methods
# Args
    # Question 9
    # Question 10

# WarmUp Questions
    # Question 11
    # Question 12
    # Question 13

# Level 1 Questions
    # Question 14
    # Question 15
    # Question 16

# Level 2 Questions
    # Question 17
    # Question 18
    # Question 19
    # Question 20 - Spy Game
# Challenging Questions
    # Question 21
    # Question 22 (incomplete)

# Homework Methods/Functions
    # Question 23 - Volume Sphere
    # Question 24 - Inside Range
    # Question 25 - Upper/Lower
    # Question 26 - Unique List
    # Question 27 - Multiply All
    # Question 28 - Palindrome
    # Question 29 - Pangram
# =================================================================
# Function Question 1:
# =================================================================

def question1():
    print("Cheese")


# =================================================================
# Function Question 2:
# =================================================================

def question2(name):
    print("Hello " + name)


# =================================================================
# Function Question 3:
# =================================================================

def question3(a):
    if a == True:
        return "Hello"
    else:
        return "Goodbye"


# =================================================================
# Function Question 4:
# =================================================================

def question4(x, y, z):
    if z == True:
        return x
    else:
        return y


# =================================================================
# Function Question 5:
# =================================================================

def question5(x, y):
    return x + y


# =================================================================
# Function Question 6:
# =================================================================

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# =================================================================
# Function Question 7:
# =================================================================

def is_greater(x, y):
    if x > y:
        return True
    else: 
        return False



# =================================================================
# Function Question 8:
# =================================================================

def question8(*args):
    return sum(args)


# =================================================================
# Function Question 9:
# =================================================================
# In order to work with the tuples that is generated from the function, you must first create an empty list in order to put the values into.
# Then you must loop through the args in order to compare each one to the associated conditions
# Lastly you must add these to the blank list if they are accepted from the conditional statement.

def question9(*args):
    evens = []
    for args in args:
        if args % 2 == 0:
            evens.append(args)
    return evens


# =================================================================
# Function Question 10:
# =================================================================
# When args is created it is created as a tuple. In order to change it over to a string so that it is editable we have
# to create a new string and .join(args) to the empty string. This passes the value of args and creates it as a string.
# Since we are pulling each letter, we can use the .capitlize() method on it in order to capital the letter if it meets the conditions.
# Lastly we add this new letter to a new string and build up the final string for submittal.

def question10(*args):
    newString = "".join(args)
    strR = ""
    index = 0
    for letters in newString:
        # conditional statement to check the index
        if index % 2 == 0:
            # if True, capitalize letter and add to new string
            # append letter to strR and move index
            strR += letters.capitalize()
            index += 1
        else:
            # append letter to strR and move index
            strR += letters
            index += 1
    return(strR)


# =================================================================
# Function Question 11: WarmUp Questions
# =================================================================

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns
# the greater if one or both numbers are odd.

# Example:
#   lesser_of_two_evens(2, 4) ==> 2
#   lesser_of_two_evens(2, 5) ==> 5

def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a, b))
        # if a < b:
        #     print(a)
        # else:
        #     print(b)
        
    else:
        print(max(a, b))
        # if a > b:
        #     print(a)
        # else:
        #     print(b)

# Test Cases: Uncomment in order to test things
# lesser_of_two_evens(12, 6)
# lesser_of_two_evens(2, 4)
# lesser_of_two_evens(2, 5)

# Notes:
# Embedded If/Else statments are used to compare the numbers and to tell if they are even or odd first, then which
# one is higher or smaller depending on where things land.

# Found after watching course explaination: The embedded IF statements can be rewritten using the min() and max()
# functions to find the larger/smaller of two numbers. 


# =================================================================
# Function Question 12: WarmUp Question
# =================================================================

# ANIMAL CRACKERS: Write a function that takes a two word string and returns True if both words begin with the same
# letter.

# Example:
#   animal_crackers("LevelHeader Llama") ==> True
#   animal_crackers("Crazy Kangaroo") ==> False

def animal_crackers(testStr):
    splitString = testStr.lower().split()
    
    print(splitString[0][0] == splitString[1][0])
    # if splitString[0][0] == splitString[1][0]:
    #     print(True)
    # else:
    #     print(False)

# Test Cases: Uncomment in order to test things
# animal_crackers("Crazy Kangaroo")
# animal_crackers("LevelHeader Llama")
# animal_crackers("Curious cat")

# Notes:
# splitString[0][0] selects the first word[0] and the first letter of that word[0].
# .split() was used to seperate each word into their own seperate string for ease of selecting.
# .lower() is used to make all the letters the same case, just in case we are comparing capital to
# lowercase letters.

# Found after watching course explaination: The if statement is not needed at all. We can just compare them
# and if its true, it will print true, if false then false.


# =================================================================
# Function Question 13: WarmUp Question
# =================================================================

# MAKES TWENTY: Given two integers, return True if the sum of the intergers is 20 or if one of the integers is 20.
# If not, return False.

# Example:
#   makes_twenty(20, 10) ==> True
#   makes_twenty(12, 8) ==> True
#   makes_twenty(2, 3) ==> True

def makes_twenty(x, y):
   print(x == 20 or y == 20 or x + y == 20)
    # if x == 20 or y == 20 or x + y == 20:
    #     print(True)
    # else:
    #     print(False)

# Test Cases: Uncomment in order to test things
# makes_twenty(20, 10)
# makes_twenty(2, 3)
# makes_twenty(12, 8)

# Notes:
# Multiple or conditions look pretty messy. Is there a way to make them look nicer?

# Found after watching course explaination: The if statement once again is redundent, if I just print the OR 
# condtionals, it will print eithe true or false based on results.


# =================================================================
# Function Question 14: Level 1 Question
# =================================================================

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

# Example:
#   old_macdonald("macdonald") ==> MacDonald

# Note: macdonald.capitlize() ==> Macdonald

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    print(first_half.capitalize() + second_half.capitalize())

    # newList = list(name.capitalize())
    # newList[3] = newList[3].upper()
    # finalList = "".join(newList)
    # print(finalList)   

# Test Cases: Uncomment in order to test things
# old_macdonald("macdonald")

# Notes:
# Not sure this is the best solution, but it does work. I have to create two new strings using this method.
# First you create a list where the first letter of the name is capitalized while turning it into a list.
# Creating the list seperates each letter out so that it can be targeted easily individually. 
# Next, you target the fourth letter (index 3) and you capitalize that letter. 
# Lastly you .join that list into a string which is returned.


# Found after watching course explaination: I need to better understand Slice commands. Basically can be done 
# with a few slices using either .capitalize() or . upper().

# =================================================================
# Function Question 15: Level 1 Question
# =================================================================

# MASTER YODA: Given a sentence, return a sentence with the words reversed.

# Example:
#   master_yoda("I am home") ==> "home am I"
#   master_yoda("We are ready") ==> "ready are We"

# Note: the .join() method may be useful here. The .join() method allows you to join together strings in a list
# with some connector string. For example, some uses of the .join() method:

# "--".join(["a", "b", "c"])
# returns: a--b--c

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a 
# single space string:

# " ".join(["Hello", "World"])
# returns: "Hello World"


def master_yoda(text):
    newList = text.split()
    newList.reverse()
    print(" ".join(newList))

# Test Cases: Uncomment in order to test things
# master_yoda("I am home")
# master_yoda("We are ready")

# Notes: Not sure why, but .reverse() appears to not be allowed inside of a print statment. I am unsure if its 
# because it changes the static direction of the list or not. Otherwise this was a fairly straight forward 
# question that I believe I figured out well.


# =================================================================
# Function Question 16: Level 1 Questions
# =================================================================

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

# Example:
#   almost_there(90) ==> True
#   almost_there(104) ==> True
#   almost_there(150) ==> False
#   almost_there(209) ==> True

# Note: abs(num) returns the absolute of a number

def almost_there(n):
    
    print((abs(n - 100) <= 10) or (abs(n - 200) <= 10))
        

# Test Cases: Uncomment in order to test things
# almost_there(104)
# almost_there(90)
# almost_there(150)
# almost_there(209)


# =================================================================
# Function Question 17: Level 2 Questions
# =================================================================

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# Example:
    # has_33([1, 3, 3]) ==> True
    # has_33([1, 3, 1, 3]) ==> False
    # has_33([3, 1, 3]) ==> False

def has_33(nums):
    counter = 0

    for num in nums:
        if num == 3:
            counter +=1
            if counter == 2:
                break
        else:
            counter = 0
    
    print(counter == 2)

# Class Example:
# def has_33(nums):
#     for i in range(0, len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             print(True)   
#     return False
    
# Notes: To start I setup a counter to track the number of 3's in a row. Looping through the set of nums I check
# it versus 3 and if true I add 1 to the counter. Now if the number is not equal to 3, I reset counter to 0.
# In order to check for two in a row, I have a second if statement which "break" out of the loop if the counter
# ever reaches 2. 2 in the counter would mean that there is a "33" in the codes. I actually had to add a 4th test
# case because I was getting the correct answer to all the three given, but, when I add numbers after the last set
# of 3's it was giving me the wrong answer. I found out this way I was running the whole loop even after hitting
# 2 on the counter and then resetting it to 0 again anyway.   


# Test Cases: Uncomment in order to test things
# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])
# has_33([3, 2, 1, 3, 3, 2, 0])


# =================================================================
# Function Question 18: Level 2 Questions
# =================================================================

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters.

# Example:
    # paper_doll("Hello") ==> "HHHeeellllllooo"
    # paper_doll("Mississippi") ==> "MMMiiissssssiiippppppiii"

def paper_doll(text):
    finalText = ""

    for letters in text:
        finalText += letters * 3

    print(finalText)

# Test Cases: Uncomment in order to test things
# paper_doll("Hello")
# paper_doll("Mississippi")

# Notes: Not sure this is the most elegant solution, but it does work.


# =================================================================
# Function Question 19: Level 2 Questions
# =================================================================

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return "Bust".

# Example
    # blackjack(5, 6, 7) ==> 18
    # blackjack(9, 9, 9) ==> "BUST"
    # blackjack(9, 9, 11) ==> 19

def blackjack(*args):
    total = sum(args)
    count = args.count(11)

    
    if total > 21 and count == 1:
        if (total - 10) > 21:
            print("Bust")
        else:
            print(total - 10)
    elif total <= 21:
        print(total)
    else:
        print("Bust")

# Test Cases: Uncomment in order to test things
# blackjack(5, 6, 7)
# blackjack(9, 9, 9)
# blackjack(9, 9, 11)
# blackjack(10, 10, 11)

# Notes: .count() returns the amount of times a search is within a list. 
# In this case, we are checking for instances of 11, which will return at least
# 1 if there is an 11 inside of the list.


# =================================================================
# Function Question 20: Level 2 Questions
# =================================================================

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore
# sections of numbers starting with a 6 and extending to the next 9.
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

# Example
    # summer_69([1, 3, 5]) ==> 9
    # summer_69([4, 5, 6, 7, 8, 9]) ==> 9
    # summer_69([2, 1, 6, 9, 11]) ==> 14

def summer_69(arr):

    # step 1: Does the list have a 6 and 9?
    if 6 in arr:
        slice6 = arr.index(6)
        slice9 = arr.index(9) + 1
        # Deletes numbers between index of 6 and index 0f 9 from list
        # Returning a new list
        del arr[slice6:(slice9)]
        
        print(sum(arr))
    # If no, sum variables
    else:
        print(sum(arr))

# Notes: arr.index() will allow me to find a particular number inside of the list.
# This should allow me to then use those index numbers to create a slice to
# remove the numbers in between if its inside of the list. 
# The del keyword allows a user to delete values from any object in python. 
# In this case, I used it to delete the values between the two indexs from my 
# list.

# Test Cases: Uncomment in order to test things
# summer_69([1, 3, 5])
# summer_69([4, 5, 6, 7, 8, 9])
# summer_69([2, 1, 6, 9, 11])
# summer_69([4, 8, 3, 6, 5, 1, 9, 7])


# =================================================================
# Function Question 21: Challenging Questions
# =================================================================

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

# Example:
    # spy_game([1, 2, 4, 0, 0, 7, 5])
    # spy_game([1, 0, 2, 4, 0, 5, 7])
    # spy_game([1, 7, 2, 0, 4, 5, 0])

def spy_game(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            print(True)
            break
    print("Only False if no true prints")
        

# Test Cases: Uncomment in order to test things
# spy_game([1, 2, 4, 0, 0, 7, 5])
# spy_game([1, 0, 2, 4, 0, 5, 7])
# spy_game([1, 7, 2, 0, 4, 5, 0])


# =================================================================
# Function Question 22: Challenging Questions
# =================================================================

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given
# number

# Example:
    # count_primes(100) ==> 25

# By convention, 0 and 1 are not prime.
def count_primes(num):
    print("working")

# Test Cases: Uncomment in order to test things
# count_primes(10)


# =================================================================
# Function Question 23: Second Set Functions/Methods
# =================================================================

# Write a function that computes the volumn of a spher given the radius

def vol(rad):
    volume = (4/3)*math.pi*rad**3
    print(volume)

# Test Cases: Uncomment in order to test things
# vol(2)

# Notes: Importing of the math library is required to use the PI function.


# =================================================================
# Function Question 24: Second Set Functions/Methods
# =================================================================

# Write a function that checks whether a number is in a given range(inclusive of high and low)
# Example:
    # ran_check(5, 2, 7) ==> 5 is in the range between 2 and 7

def ran_check(num, low, high):
    newRange = range(low, high + 1)
    if num in newRange:
        print(f"{num} is in range between {low} and {high}")
    else:
        print(f"{num} is not in the range of {low} and {high}")

# If you only wanted to return a boolean

def ran_bool(num, low, high):
    newRange = range(low, high + 1)
    if num in newRange:
        print(True)
    else:
        print(False)

# Test Cases: Uncomment in order to test things
# ran_check(5, 2, 7)
# ran_check(10, 1, 9)
# ran_bool(3, 1, 10)
# ran_bool(10, 1, 9)

# =================================================================
# Function Question 25: Second Set Functions/Methods
# =================================================================

# Write a function that accepts a string and calculates the number of uppercase and lowercase letters.

# Example:
    # Sample String: "Hello Mr. Rogers, how are you this fine Tuesday?"
    # No. Uppercase characters: 4
    # No. Lowercase characters: 33

def up_low(s):
    upperCount = 0
    lowerCount = 0

    for i in s:
        if i.isupper() == True:
            upperCount += 1
        elif i.islower() == True:
            lowerCount += 1
    
    print(f"No. of Uppercase Characters: {upperCount}")
    print(f"No. of Lowercase characters: {lowerCount}")

# Test Cases: Uncomment in order to test things
s = "Hello Mr. Rogers, how are you this fine Tuesday?"
# up_low(s)


# =================================================================
# Function Question 26: Second Set Functions/Methods
# =================================================================

# Write a python function that takes a list and returns a new list with unique elements of the first list

# Example:
    # Sample List: [1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5]
    # Unique List: [1, 2, 3, 4, 5]

def unique_list(lst):
    uniqueSet = set(lst)
    print(uniqueSet)

# Test Cases: Uncomment in order to test things
# unique_list([1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5])

# Notes: Sets take in a list and returns a unique list of the variables. 


# =================================================================
# Function Question 27: Second Set Functions/Methods
# =================================================================

# Write a Python function to multiply all the numbers in a list
# Example:
    # Sample List: [1, 2, 3, -4] ==> -24

def multiply(nums):
    result = 0
    for i in nums:
        if result == 0:
            result = i
        else:
            result *= i
    print(result)

# Test Cases: Uncomment in order to test things
# multiply([1, 2, 3, -4])


# =================================================================
# Function Question 28: Second Set Functions/Methods
# =================================================================

# Write a Python function that checks whether a passed in string is a palindrome or not.

# Note: A palindrome is a word, phrase, or sequence that reads the same backwards as forwards.
# Example:
    # madam
    # nurses run 
    # abby
    # 1221

def palindrome(s):
    reverseWord = s[::-1]
    print(reverseWord == s)

# Test Cases: Uncomment in order to test things
# palindrome("helleh")
# palindrome("cheese")


# =================================================================
# Function Question 29: Second Set Functions/Methods
# =================================================================

# Write a python function to check whether a string is a pangram or not.

# Note: Pangrams are words or sentences container every letter of the alphabet at least once.
# Example: "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module

def isPangram(str1, alphabet=string.ascii_lowercase):
    print("working")