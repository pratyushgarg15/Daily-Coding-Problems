'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the 
first and last element of that pair. For example, car(cons(3, 4)) returns 3,
and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.

'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    print(f)
    return f(lambda a, b : a)

def cdr(f):
    return f(lambda a, b : b)
    
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    if(car(cons(a,b)) == a):
        print('yes')
    if(cdr(cons(a,b)) == b):
        print('yes')   
