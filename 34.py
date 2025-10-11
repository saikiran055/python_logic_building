#Check if a number is prime.
a=int(input("enter number:"))
count=0
for i in range(1,a+1):
  if a%i==0:
    count+=1
if count==2 or count==1:
  print(f"{a} is prime")
else:
  print(f"{a} is not a prime")
