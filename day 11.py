'''
Objective
Today, we are building on our knowledge of arrays by adding another
dimension. Check out the Tutorial tab for learning materials and an
instructional video.
Context
Given a 6 x 6 2D Array, A:

We define an hourglass in A to be a subset of values with indices falling
in this pattern in A's graphical representation:
There are 16 hourglasses in A, and an hourglass sum is the sum of an
hourglass' values.
Task
Calculate the hourglass sum for every hourglass in A, then print the
maximum hourglass sum.
Example
In the array shown above, the maximum hourglass sum is 7 for the
hourglass in the top left corner.
Input Format
There are 6 lines of input, where each line contains 6 space-separated
integers that describe the 2D Array A.
Constraints
Output Format
Print the maximum hourglass sum in A.
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max=-10000
    for i in range(4):
        for j in range(4):
            sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if sum > max:
                max=sum
    print(max)
