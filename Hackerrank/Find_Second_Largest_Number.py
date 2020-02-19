'''

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Input Format :
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints :
    2 <= n <= 10
    -100 <= A[i] <= 100
    
Output Format :
Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5

Explanation 0
Given list is [2,3,6,6,5]. The second maximum is 5. Hence, we print 5 as the runner-up score.

'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max=max(arr[0],arr[1])
    min=min(arr[0],arr[1])
    for i in range(2,len(arr)):
        if(min==max and arr[i]<min):
            min=arr[i]
        elif(arr[i]>max):
            min=max
            max=arr[i]
        elif(arr[i]>min and arr[i]!=max):
            min=arr[i]
    print(min)
