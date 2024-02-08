import random 
n = int(input())
print("""Hello! What is your name?
      KBTU
Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.""")
m = 0
def aliko(n):
    global m
    m1 = random.randint(1, 2*n)
    m = m + 1
    if n == m1:
        print(m1)
        print("Good job, KBTU! You guessed my number in " + str(m) + " guesses!")
    else:
        print(m1)
        aliko(n)

aliko(n)