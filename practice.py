# =================================================================
# Function Question Index:
# =================================================================
# Generally questions with notes are fully explained questions.

# Jose Portilla Python Bootcamp
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