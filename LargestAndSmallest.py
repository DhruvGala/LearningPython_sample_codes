# @author DhruvGala
# The following code calculates the maximum and the
# minimum of the integers that are given as the input
# This code is just to demonstrate the nested conditional loop
# using Python.

largest_so_far = -1
smallest_so_far = None


# goes to infinte loop until the input by the user is
# a string "done".
while True:
    input = raw_input("Enter a number: ")
    if input == "done":
        break
    
    else:
        # the following code is the logic of converting string to number
        # using tru catch block for handelling exceptions.
        try:
            number = int(input)
        except:
            print("Invalid input")
            continue
    
    #this is the basic logic of determining the largest of the numbers.
    if number > largest_so_far:
        largest_so_far = number
    if smallest_so_far is None:
        smallest_so_far = number
    elif number < smallest_so_far:
        smallest_so_far = number

#printing the output.        
print "Maximum is", largest_so_far
print "Minimum is", smallest_so_far