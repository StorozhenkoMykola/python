# task_1
list_1=[]
i=0
while i<10:
    a=int(input("enter number= "))
    list_1.append(a)
    i+=1
print(list_1)
max=0
min=0
for m in list_1:
    if max<m: max=m
    if min>m: min=m
print("min = ",min,"max = ",max)


# task_2

print([x for x in range(1,11) if x%2==0],"Діляться на 2" )
print([x for x in range(1,11) if x%3==0],"Діляться на 3" )
print([x for x in range(1,11) if x%3==1 and x%2==1],"Не діляться ні на 2, ні на 3" )

# task_3

a=int(input("enter number= "))
f=1
for i in range(1,a+1):
    f*=i
print("Факторіал числа = ", f)

# task_4

login="First"
a=input("Введіть логін ")
if a==login:
    print("Welcome!")
while a!=login:
    print('error')
    break

# task_5

i=0
while i==0:
    a=int(input("enter number "))
    if a<=0:
        print ("your number is negative or 0")
        i+=1

# task_6

n=int(input("enter number of numbers"))
i=1
while n>=i:
    a=int(input("enter number "))
    if a<=0:
        print ("your number is negative or 0")
        break
    i+=1