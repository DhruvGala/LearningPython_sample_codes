'''
Created on Oct 10, 2015

@author: DhruvGala

The following code is a general implementation of Tower of hanoi problem using python 3.
'''
from pip._vendor.distlib.compat import raw_input

'''
The following method carries out the recursive method calls to solve the 
tower of hanoi problem.
'''
def towerOfHanoi(number,source,inter,dest):
    if(number == 1):
        print("Disk 1 from {} to {} ".format(source,dest))
        
    else:
        towerOfHanoi(number-1, source, dest, inter)
        print("Disk {} from {} to {}".format(number,source,dest))
        towerOfHanoi(number-1, inter, source, dest)
    
'''
the main method
'''    
def main():
    towerOfHanoi(takeInput(),"A","B","C")
    
'''
takes the input as the number of disk involved in the problem.
'''    
def takeInput():
    n = raw_input("Enter the number of disks: ")
    try:
        nDisk = int(n)
    except:
        print("Invalid input")
     
    return nDisk;
    
#call the main method        
if __name__ == "__main__": main()   