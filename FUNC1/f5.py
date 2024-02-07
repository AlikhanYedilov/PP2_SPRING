from itertools import permutations
s = input()
def aliko(s):
    ans = permutations(s)
    for i in ans:
        print(''.join(i))

aliko(s)