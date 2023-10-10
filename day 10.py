'''
Objective
Today, we're working with binary numbers. Check out the Tutorial tab
for learning materials and an instructional video!
Task
Given a base-IO integer, n, convert it to binary (base-2). Then find and
print the base-IO integer denoting the maximum number of
consecutive I's in n's binary representation. When working with
different bases, it is common to show the base as a subscript.
Example
n = 125
5 and 1 consecutive ones in two groups. Print the maximum, 5.
Input Format
A single integer, n.
Constraints
• 106
Output Format
Print a single base-10 integer that denotes the maximum number of
consecutive I's in the binary representation of n.
Sample Input 1
5
Sample Output 1
1
Sample Input 2
13
Sample Output 2
2
Explanation
Sample Case 1:
The binary representation of 510 is 1012, so the maximum number of
consecutive I's is 1.
Sample Case 2:
The binary representation of 1310 is 11012, so the maximum number
of consecutive I's is 2.
'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bin_num_str= bin(n)
    bin_num=bin_num_str[2:]
    list=bin_num.split('0')
    max=-1
    for i in list:
        if len(i)>max:
            max=len(i)
    print(max)
