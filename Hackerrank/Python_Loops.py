'''

Task :
Read an integer N. For all non-negative integers i<N, print i^2. See the sample for details.

Input Format :
The first and only line contains the integer, N.

Constraints :
    1 <= N <= 20

Output Format :
Print N lines, one corresponding to each i.

Sample Input 0
5

Sample Output 0
0
1
4
9
16

'''

a = int(input())
i=0
while(i<a):
    print(i**2)
    i+=1

#Another method
#print(*[i**2 for i in range(a)], sep='\n')
