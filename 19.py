#Find the compound interest.
p,r,t=input("Principal_amount,Annual_interest_rate,Time_in_years:").split()
p=float(p)
r=float(r)
t=float(t)
ci=(p*(1+r/100)**t)-p
print("compound interest is:",ci)
