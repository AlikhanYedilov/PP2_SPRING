n = int(input())#number of ints
sum = int(input())
f = False
for i in range(n - 1):
    n1 = int(input())
    if n1 == 3:
        if sum == n1:
            f = True
    sum = n1        

print(f)