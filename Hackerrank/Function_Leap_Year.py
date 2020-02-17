'''

We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
A year is leap year if the following conditions are satisfied:
    1. Year is multiple of 400.
    2. Year is multiple of 4 and not multiple of 100

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Task :
You are given the year, and you have to write a function to check if the year is leap or not.

Input Format :
Read y, the year that needs to be checked.

Constraints :
    1900 <= y <= 10^5

Output Format :
Your function must return a boolean value (True/False)

Sample Input 0
1990

Sample Output 0
False

'''

def is_leap(year):
    leap = False
    if(year%400==0 or (year%4==0 and year%100!=0)):
        leap = True
    return leap
    
year = int(input())
print(is_leap(year))
