#Find the sum of digits of a number.
n=int(input("enter number:"))
sum=0
while(n!=0):
  rem=n%10
  sum+=rem
  n//=10
print(f"sum of digits of {n} are {sum}")
