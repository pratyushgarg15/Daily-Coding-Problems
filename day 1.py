'''Given a list of numbers and a number k, return whether any two numbers
 from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def sumUP(arr, k):
    d = {}
    d[arr[0]] = True
    for i in range(1,len(arr)):
        if k-arr[i] in d:
            return True
        else:    
            d[arr[i]] = True
        
    return False

arr = list(map(int,input().split(' ')))
k = int(input())

print(sumUP(arr , k))
    