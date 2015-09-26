# @author DhruvGala
# The following code calculates the sum, count and the
# average of the integers that are given as the input

total = 0
count = 0

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
            number = float(input)
        except:
            print("Invalid input")
            continue
    
    # Keeps track of sum and the count of the integers entered by the
    # user so far.    
    total = total + number
    count = count + 1     

# prin the output to the screen
print "sum:", total
print "count:", count
print "average:", (total/count)    