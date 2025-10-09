# Find the sum of first N even numbers
n=int(input("enter number"))
sum=0
for i in range(0,n+1):
    if (i%2==0):
        sum+=i
print(f"sum of first {n} even numbers are:{sum}")
