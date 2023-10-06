'''
Objective
Today we will expand our knowledge of strings, combining it with what
we have already learned about loops. Check out the Tutorial tab for
learning materials and an instructional video.

Task
Given a string, S, of length N that is indexed from O to N — I, print its
even-indexed and odd-indexed characters as 2 space-separated strings
on a single line (see the Sample below for more detail).
Note: O is considered to be an even index.

Example
s adbecf
Print abc def
Input Format
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.

Constraints
• 10
• 2 length of S < 10000
Output Format
For each String Sj (where 0 j < T — 1), print Sj's even-indexed
characters, followed by a space, followed by Sj's odd-indexed
characters.

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for j in range(T):
    S=input()
    N=len(S)
    str1=""
    str2=""
    for i in range(N):
        if i % 2==0:
            str1=str1 + S[i]
        else:
            str2=str2 + S[i]
    print(str1+" "+str2)
