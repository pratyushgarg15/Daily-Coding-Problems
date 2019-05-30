'''Given an array of integers, return a new array such that each element 
at index i of the new array is the product of all the numbers in the 
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would 
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output 
would be [2, 3, 6].'''


def multiplicative(arr):
    pre = [1 for i in range(len(arr))]
    post = [1 for i in range(len(arr))]
    result = [0 for i in range(len(arr))]
    
    for i in range(1,len(pre)):
        pre[i] = pre[i-1] * arr[i-1]
        
    for i in range(len(post)-2,-1,-1):
        post[i] = post[i+1] * arr[i+1]
        
    for i in range(len(result)):
        result[i] = pre[i] * post[i]
        
    return result    
    

if __name__ == '__main__':
    arr = list(map(int,input().split(' ')))
    print(multiplicative(arr))    