'''

Task :
Read a given string, change the character at a given index and then print the modified string.

Input Format :
The first line contains a string, S.
The next line contains an integer i, denoting the index location and a character c separated by a space.

Output Format :
Replace the character at index i with character c.

Sample Input
abracadabra
5 k

Sample Output
abrackdabra

'''

#Method 1
'''
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
'''
#Method 2
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
