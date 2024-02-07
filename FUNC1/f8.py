n = int(input())#number of ints
sum1 = int(input())
sum2 = int(input())
f = False
for i in range(n - 2):
    n1 = int(input())
    if sum1 == sum2 and sum1 == 0 and n1 == 7:
        f = True
    sum1 = sum2   
    sum2 = n1   

print(f)