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
# Embedded If/Else statments are used to compare the numbers and to tell if they are even or odd first, then which one is higher or smaller depending on where things land.

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
    newList = list(name.capitalize())
    newList[3] = newList[3].upper()
    finalList = "".join(newList)
    print(finalList)   

# Test Cases: Uncomment in order to test things
# old_macdonald("macdonald")

# Notes:
# Not sure this is the best solution, but it does work. I have to create two new strings using this method.
# First you create a list where the first letter of the name is capitalized while turning it into a list.
# Creating the list seperates each letter out so that it can be targeted easily individually. 
# Next, you target the fourth letter (index 3) and you capitalize that letter. 
# Lastly you .join that list into a string which is returned.
