'''

Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format :
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints :
    2 <= N <= 5
    There will always be one or more students having the second lowest grade.

Output Format :
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

'''
#Method 1
if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list=[score,name]
        l.append(list)
    l.sort()
    min=l[0][0]
    for i in range(1,len(l)):
        if(l[i][0]>min):
            min=l[i][0]
            break
    print(*[i[1] for i in l if i[0]==min],sep='\n')
    
    
#Method 2
l = []
for _ in range(0,int(input())):
    l.append([input(), float(input())])
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
