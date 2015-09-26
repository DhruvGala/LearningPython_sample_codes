# @author: DhruvGala
# The following is a Python code for determining most emails received 
# from a particular sender email id, amongst the senders which are 
# documented in a text file named: 'mbox-short.txt'.

filename = raw_input("Enter file name: ")
filehandle = open(filename)

# use of the dictionary to keep track of counts of each email id with
# a corresponding mail received.
counts = dict()
emails = list()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    #print "line-->",line
    words = line.split()
    #print "words-->",words
    emails.append(words[1])

# gets the count of each email id.    
for email in emails:
    counts[email] = counts.get(email,0) + 1
    
mostEmails = None
howMany = None

# find the email id with the most counts.
for email,count in counts.items():
    #print email,count
    if howMany is None or count > howMany:
        mostEmails = email
        howMany = count

print mostEmails, howMany