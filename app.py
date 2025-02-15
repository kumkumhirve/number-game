import random 

x = random.randint(1,10)
y = ""

attempt = 0
while x != y :
    y = int(input("enter your number between 1 to 10 : "))
    attempt += 1
    if x == y:
        print("congrats,you won")
        print("attempts are taken by you : {attempt}")
    elif x > y :
        print("too, small")
    elif x <y:
        print("too big")
