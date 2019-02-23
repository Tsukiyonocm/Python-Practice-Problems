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
# Function Question 11:
# =================================================================

