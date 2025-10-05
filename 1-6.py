a,b=input("enter 2 inputs with space:").split()
print("addition:",int(a)+int(b))
print("subtraction:",int(a)-int(b))
print("multiplication:",int(a)*int(b))
print("quotient:",int(a)/int(b))
print("remider:",int(a)%int(b))
print("before swaping",int(a),int(b))
c=a
a=b
b=c
print("after swaping",int(a),int(b))
