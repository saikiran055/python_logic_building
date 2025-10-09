#Find the sum of first N natural numbers.
#Find the sum of first N even numbers
#Find the sum of first N odd numbers
n=int(input("enter number"))
sum1=sum2=sum3=0
for i in range(0,n+1):
    sum1+=i
    if (i%2==0):
        sum2+=i
    else:
        sum3+=i
print(f"sum of first {n} natural numbers are:{sum1}")
print(f"sum of first {n} even numbers are:{sum2}")
print(f"sum of first {n} odd numbers are:{sum3}")
