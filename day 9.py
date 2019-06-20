"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of 
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""

def maxNonAdjacentSum(arr):
    inc = 0
    excl = 0
    
    for i in range(len(arr)):
        temp = inc
        inc = excl + arr[i]
        excl = max(temp,excl)
        
    return max(inc,excl)

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    print(maxNonAdjacentSum(arr))    