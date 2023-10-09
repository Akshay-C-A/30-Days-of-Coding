'''
Objective
Today, we are learning about an algorithmic concept called recursion.
Check out the Tutorial tab for learning materials and an instructional
video.
Recursive Method for Calculating Factorial
1
factorial(N)
N x factorial(N — 1) otherwise
Function Description
Complete the factorial function in the editor below. Be sure to use
recursion.
factorial has the following paramter:
• int n: an integer
Returns
• int: the factorial of n
If you fail to use recursion or fail to name your recursive function
Note:
factorial or Factorial, you will get a score of 0.
Input Format
A single integer, n (the argument to pass to factorial).
Constraints
2 < n < 12
• Your submission must contain a recursive function named factorial.
Sample Input
3
Sample Output
6
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    fact = 0
    if n<=1:
        return 1
    else:
        fact += n*factorial(n-1)
    return fact
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
