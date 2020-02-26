'''

Given a full name, your task is to capitalize the name appropriately.

Input Format :
A single line of input containing the full name, S.

Constraints :
    0 < len(S) < 1000
    The string consists of alphanumeric characters and spaces.

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format :
Print the capitalized string, .

Sample Input
chris alan

Sample Output
Chris Alan

'''
#Method 1
def solve(s):
    return s.title()

#Method 2
'''
def solve(s):
    for x in s[:].split():
        s = s.replace(x,x.capitalize())
    return s
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
