#Find the sum of first N natural numbers.
n=int(input("enter number"))
sum=0
for i in range(1,n+1):
  sum+=i
print(f"sum of first {n} natural numbers are:{sum}")
