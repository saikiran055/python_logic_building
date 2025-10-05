#Find the largest of three numbers.
a,b,c=input("enter inputs with space:").split()
if a<b:
    if c<b:
        print("second input is greatest")
    else:
        print("third input is largest")
else:
    if c<a:
        print("first input is greatest")
    else:
        print("third input is greatest")
