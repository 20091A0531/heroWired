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
