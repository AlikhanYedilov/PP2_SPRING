list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]#can be made on diff
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def aliko(list):
    return [n for n in list if prime(n)]

print(aliko(list))