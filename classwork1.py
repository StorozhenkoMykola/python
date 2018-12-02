a=int(input("enter number a = "))
b=int(input("enter number b = "))
if (b>a): print("bigger number b = "+str(b))
elif (b<a): print("bigger number a = "+str(a))
else:print ("a=b")


a=int(input("enter number "))
if (a%2): print("Не парне число")
else:print("Парне число")

a=int(input("enter number = "))
i = 1
f = 1
while i <= a:
    f *= i
    i += 1
print("factorial of number ",a, " = ", f)