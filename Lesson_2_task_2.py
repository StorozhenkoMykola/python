number=input("enter number = ")
p=1
r=""
for n in number:
    p=int(n)*p
    r=n+r
print("prodact = ",p)
print("revers = ",r)
print("sort = ",sorted(r))