n = [1,1,2,3,4,5,6,7,7,8,8]
def aliko(n):
    n1 = []
    for i in n :
        if i not in n1:
            n1.append(i) 
    print(n1)

aliko(n)