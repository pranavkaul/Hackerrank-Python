def minion_game(string):
    vowel = ['A','E','I','O','U']
    stuart_score = 0
    kevin_score = 0
    l = len(string)
    for i in range(l):
        if string[i] in vowel:
            kevin_score = kevin_score + (l - i)
        else:
            stuart_score = stuart_score + (l - i)
    if kevin_score > stuart_score:
        print('Kevin {}'.format(kevin_score))
    elif stuart_score > kevin_score:
        print('Stuart {}'.format(stuart_score))
    else:
        print('Draw')

            
if __name__ == '__main__':
    s = input()
    minion_game(s)
