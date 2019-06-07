'''
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n,
and calls f after n milliseconds.
'''

import time

def jobscheduler(f, n):
	time.sleep(n/1000)
	return f()

if __name__ == '__main__':
    n = int(input())
    while(n):
        print(jobscheduler(lambda: "Hi! " + time.ctime(), 2000))
        n-=1