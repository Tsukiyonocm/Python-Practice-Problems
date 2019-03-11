Python Learning


    .split() Function
The .split() function will take an argument and will break apart a string based on teh context of the argument. For instance:

            string = "This is a string"
            string.split()
            Output = ["This", "is", "a", "string"]

The output of the above string using a blank argument seperates at the first whitespace of the text. 


    Slice
Using the slice functionality is as easy as telling python how far you wish to slice at any given moment.
            string = "Bacon"
            string[0]
            Output = ["B"]

            string[1]
            Output = ["a"]

            string[0:2]
            Output = ["Ba"]
The first number is how many spaces you wish to start with. 0 meaning starting at first letter in the case of a string, 1 being second letter and so on. The :integer then means how many spaces to move out from there. It must be said that you are starting from the beginning of the letters. So things start at left of "B" and continue so moving 2 spaces gives us "Ba" in last example.


    len()
This works similar to Javascript in where its a function that finds out the length of the string or object that is connected to it. Unlike javascript though, this is not tacked onto the end of the variable name. In python the syntax is as follows:
            varName = "string"
            len(varName)
            Output = 6

<!-- TODO -->
<!-- Create a index at the top of all the things I am typing in here for quicker use cases. -->
<!-- Figure out how to make the markup look better. Maybe move this over to html/css in the future -->