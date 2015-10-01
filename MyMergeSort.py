'''
Created on Oct 1, 2015

@author: DhruvGala 

The following code is a general implementation of merge sort using Python.
   
'''
from pip._vendor.distlib.compat import raw_input

'''
The following code is the main logic of implementing the merge sort.
'''
def mergeSort(alist):
    
    #Initially we split the list that has been passed.
    if len(alist)>1:
        middle = len(alist)//2
        left_half = alist[:middle]
        right_half = alist[middle:]

        mergeSort(left_half)
        mergeSort(right_half)
        
        #we then merge the passed list while arranging them in the sorted order.
        i,j,k=0,0,0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k]=left_half[i]
                i=i+1
            else:
                alist[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):
            alist[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):
            alist[k]=right_half[j]
            j=j+1
            k=k+1
    
    return alist


'''
The following method takes the input from the user.
'''
def takeInput():
    s = raw_input('Enter the numbers separated by space in between: ')
    numbers = list(s.split(sep=' '))
    numbers = [int(i) for i in numbers]
    return numbers
        
'''
the main method
'''
def main():
    
    sortedlist = mergeSort(takeInput())
    print("Sorted list:", sortedlist)

#call the main method        
if __name__ == "__main__": main()        