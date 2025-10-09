# Generate multiplication table of a number.
n=int(input("enter number"))
print(f"multiplication table of {n}is:")
for i in range(1,11):
  print(f"{n}*{i}={n*i}")
