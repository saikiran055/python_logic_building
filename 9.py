#Find the largest of two numbers.
a,b=input("enter inputs with space:").split()
if a<b:
    print("first input is greatest")
elif a==b:
    print("both inputs are equal")
else:
    print("second input is greatest")
