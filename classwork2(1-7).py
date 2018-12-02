#task1
i=0
while i<100:
    print(i)
    i+=2
for a in range(100):
    if a%2==0: 
        print(a)

#task2
i=1
while i<100:
    if i%2==1:
        print(i)
        i+=2
a=1
while a<100:
    if a%2==0:
        continue
    print(a)
    a+=2

#task3
list_1=[2,4,6,8,9]
y=0
m=0
while m<len(list_1):
    if list_1[m]%2==1:
        y=1
        break
    m+=1
if y==0:print("Список не містить тільки парні числа")
else:print("Список містить непарні числа")

#task4
list_1=[1,4,45,89]
i=0
for a in list_1:
    list_1[i]=float(a)
    i+=1
print(list_1)

#task5
a=int(input("enter number = "))
m=0
n=1
s=0
while m<a:
    print (m)
    s=m+n
    n=m
    m=s

#task6
list_1 = ['a', 'b', 'c', 'd']
for i in list_1:
    print (i)

#task7
list_1 = ['a', 'b', 'c', 'd']
m=0
for i in list_1:
    print ("\n",i,end="#")