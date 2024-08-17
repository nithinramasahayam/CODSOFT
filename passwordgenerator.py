print("     PASSWORD GENERATOR     ")
import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
symbols="!@#$%^&*()[]{}?\/;:.,"
all=upper+lower+digits+symbols
#taking input from user for length of password
length=int(input("Enter the length of password required : "))
#taking input from user for no of passwords required
amount=int(input("Enter the no of passwords required : "))
for i in range(amount):
    password="".join(random.sample(all,length))
    print("The Generated password is")
    print(password)  