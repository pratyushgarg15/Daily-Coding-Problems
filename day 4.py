"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.
"""


def lowest_integer2(arr):
    maximum = arr[0]
    hash_table = {}
    
    for i in range(1,len(arr)):
        if(arr[i] > maximum):
            maximum = arr[i]
            
    minimum = maximum
    
    for i in range(len(arr)):
        if(arr[i] < minimum and arr[i] > 0):
            minimum = arr[i]
    
    '''if min positive integer is not 1 return 1'''
    if (minimum != 1):
        return 1
    
    '''create a hash table with the elements of the array as key'''
    for val in arr:
        hash_table[val] = 1
    
    '''loop over numbers from min +ve integer to max +ve integer 
       and return the first element that is not in the hash table'''
    for i in range(minimum+1,maximum):
        if i not in hash_table:
            return i
    
    '''if numbers from min to max are contiguous return max+1'''
    return maximum+1

def lowest_integer1(arr):
     
    j = len(arr)-1
    count = 0
    maximum = max(arr)
    
    '''segregate and shift all negative integers to the left 
       side of the array'''
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]<=0):
            arr[i] , arr[j] = arr[j] , arr[i]
            j-=1
            count+=1

    '''mark indices negative signifying that an element is 
       present in the array'''        
    for i in range(0,len(arr)-count):
        if(abs(arr[i])-1 < len(arr) and arr[abs(arr[i])-1] > 0):
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    
    '''return the index + 1 of first element that is not negative'''
    for i in range(len(arr)):
        if(arr[i]>0):
            return i+1
        
    return maximum+1    
            


if __name__ == '__main__':
    arr = list(map(int,input().split(' ')))
    print(lowest_integer1(arr))
