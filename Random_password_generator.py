import random
import string
while True:
    n=int(input("Enter Length of the Password for to generate: "))
    k=string.digits+string.punctuation+string.ascii_letters
    password=""
    for i in range(n):
         password=password+random.choice(k)
    print("The Password is:",password)
    ch=input("Do you Want to Regenerate Y/N:")
    if ch.lower()!="yes" and ch.lower()!="y":
        break