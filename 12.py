#Check if a number is divisible by 2 and 3.
a=int(input("enter input:"))
if a%2==0:
    if a%3==0:
        print("input is divisible by both 2 and 3")
    else:
        print("input is divisible by 2 but not by 3")
elif a%2!=0:
    if a%3==0:
        print("input is divisible by 3 but not by 2")
    else:
        print("input is not divisible by both 3 and 2")
