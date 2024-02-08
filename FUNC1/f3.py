def aliko3(a, b):
    return ((b - 2*a) / 2)

a = int(input())
b = int(input())

print(aliko3(a, b))#rabbits
print(((a + b) - (aliko3(a,b) * 5))/3)