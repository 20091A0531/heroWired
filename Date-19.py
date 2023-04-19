1
22
333
4444
55555
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
  for j in range(i+1):
    print(i,end="")
  print()

------------------------
-->reversing  a number and checking if it is palindrome


num=int(input("enter a number"))
temp=num
rev=0
while(temp!=0):
  rem=temp%10
  rev=rev*10+rem
  temp=temp//10
if(num==rev):
  print("It is a palindrome")
else:
  print("It is not a palindrome")
------------------------
Armstrong number

num=int(input("enter a number"))
amg=0
temp=num
while(temp!=0):
  rem=temp%10
  amg=amg+rem*rem*rem
  temp=temp//10
if(num==amg):
  print("It is a Armstrong number")
else:
  print("It is not a Armstrong number")
---------------------------
area of triangle,square,rectangle

i=1
while(i<=3):
  if(i==1):
    h=int(input("Enter the height for the area of triangle:"))
    b=int(input("Enter the breadth of the triangle:"))
    print("area of triangle is {}".format(0.5*h*b))
  elif(i==2):
    s=int(input("Enter the side of the square:"))
    print("area of square is {}".format(s*s))
  else:
    l=int(input("Enter the length for the area of rectangle:"))
    b=int(input("Enter the breadth of the rectangle:"))
    print("area of rectangle is {}".format(l*b))
  i+=1
----------------------------
swaping three numbers in ascending order

a=int(input("Enter the number1"))
b=int(input("Enter the number2"))
c=int(input("Enter the number3"))
l3=0
l2=0
l1=0
if(a>c and a>b):
  l3=a
  if(b<c):
    l1=b
    l2=c
  else:
    l1=c
    l2=b
elif(b>c and b>a):
  l3=b
  if(a<c):
    l1=a
    l2=c
  else:
    l1=c
    l2=a
else:
  l3=c
  if(b<a):
    l1=b
    l2=a
  else:
    l1=a
    l2=b
a,b,c=l1,l2,l3
print(a,b,c)

-----------------------------
fibanocci series


n=int(input("Enter the number,upto where you want the fibanocci numbers:"))
a=0
b=1
print(a,b,end=" ")
while(a+b<n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

-----------------------
