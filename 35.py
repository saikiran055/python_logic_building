#Find all prime numbers between 1 and N.
n=int(input("enter number:"))
count=0
for i in range(1,n+1):
  for j in range(1,n+1):
    if i%j==0:
      count+=1
  if count==2:
    print(i)
  count=0
