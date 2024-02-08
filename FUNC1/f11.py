s = input()
sum = len(s) 
check = 1
def aliko(s):
    for i in sum:
        if(s[i] != s[sum - 1]):
            check = 0
            sum = sum - 1
    return check
ali = aliko(s)
if ali == 0:
    print("not palindrome")
else:
    print("polindrome")