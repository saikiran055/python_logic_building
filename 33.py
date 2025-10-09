#Check if a number is palindrome.
s=input("enter value:")
b=s[::-1]
if s==b:
  print(f"{s} is a palindrome")
else:
  print(f"{s} is not a palindrome")
