def aliko(a, b):
    return ((b - 2*a) / 2)

a = int(input())
b = int(input())

print(aliko(a, b))#rabbits
print(((a + b) - (aliko(a,b) * 5))/3)