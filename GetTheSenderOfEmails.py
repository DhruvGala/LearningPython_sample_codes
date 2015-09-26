# @author: DhruvGala
# The following is a Python code for determining the sender of emails
# which are documented in a text file named: 'mbox-short.txt'.

filename = raw_input("Enter file name: ")

# the filehandle is used to operate the I/O operations
filehandle = open(filename)

#fetch each line from the file
for line in filehandle:
    line = line.rstrip()

    # if the line starts with 'from', then fetch the email 
    # address following it
    if not line.startswith('From '): 
    	continue
    #print "line-->",line
    
    words = line.split()
    #print "words-->",words
    
    print words[1]