# @author: DhruvGala
# The following is a Python code for counting the hours at which the 
# emails were received from the respective senders.

filename = raw_input("Enter file name: ")
filehandle = open(filename)

# use of the dictionary to keep track of counts of time at which 
# each email was received.
counts = dict()
hour = list()
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    #print "line-->",line
    words = line.split()
    #print "words-->",words
    time = words[5].split(':')
    hour.append(time[0])

# The foloowing for loop gets the count of each email reception.    
for hrs in hour:
    counts[hrs] = counts.get(hrs,0) + 1
    
#print counts
t = counts.items()
t.sort()

# print using key value pairs from the dictionary data structure.
for key,val in t:
    print key, val