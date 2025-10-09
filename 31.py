# Reverse a number ignoreing front and ending 0's.
n=int(input("enter number:"))
n=int(n)
rev=0
print(f"the reverse of {n} is:")
while(n!=0):
  rem=n%10
  rev=rev*10+rem
  n=n//10
print(f"{rev}")
# Reverse a number including all 0's.
n=input("enter number:")
b=n[::-1]
print(b)
