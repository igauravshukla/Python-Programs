'''

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules :
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring :
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

'''

def minion_game(string):
    sp , kp = 0 ,0
    for start in range(len(string)):
        i=string[start]
        if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            kp+=(len(string)-start)
        else:
            sp+=(len(string)-start)
    if(sp>kp):
        print("Stuart",sp)
    elif(sp<kp):
        print("Kevin",kp)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
