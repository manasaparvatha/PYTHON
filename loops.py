#print numbers from 1to 10
for i in range(1,11):
    print(i)

#print odd number from 1to 50
for i in range(1,51,2):
            print(i)

#print even number from 1to 50
for i in range(0,51,2):
    print(i)

for i in range(5,51,5):
    print(i)

#multiplication tables
#number=int(input("enter number:"))
#
# for i in range(1,11):
  #  print(number,"x",i,"=",number*i)

    #sum of numbers from 1 to n
#n=int(input("enter number n:"))
#total=0
#for i in range(1,n+1):
#  total=total+i
#print("sum:",total)

#factorial of a number
#n=int(input("enter number:"))
#factorial=1
#for i in range(1,n+1):
 # factorial=factorial*i
#  print("factorial:",factorial)


#sum of 
#n=int(input("enter n:"))
#total=0
#for i in range(2,n+1,2):
#    total=total+i
#    print("sum:",total)

#count of multiple of 3
#    n=int(input("enter n:"))
#    count=0
#    for i in range(1,n+1):
#        if i % 3==0:
#            count = count+1
#            print("count:",count)

#sum of multiple of 5
#n=int(input("enter n:"))
#sum=0
#for i in range(1,n+1):
#    if i % 5==0:
 #         total=total+i
 #   print("sum:",total)
    
 #print all even numbers from 2to 50
  #  i=2
  #  while i <=50:
 #       print(i)
 #       i=i+2


# print all odd numbers from 2to 50
 #   i=2
#    while i <=50:
  #      print(i)
  #      i=i+1


#total=0
#number=int(input("enter number:"))
#while number !=0:
#    total = total +number 
 #   number=int(input("enter number"))


#password check
#    password=""
 #   while password !="python123":
 #       password=input("enter password:")
 #       print("iogin sucessfull:")

#count the number of digits in a number
#number=int(input("enter number:"))
#count=0
#while number>0:
#number=number//10
#count=count+1
#   print("number of digits:",count)


#sum of digites in a number
number=int(input("enter number:"))
sum=0
while number>0:
    digit=number%10
    number=number//10
    sum=sum+ digit
    print("sum of digits:",sum)


#reverse number
number=int(input("enter number:"))
reverse=0
while number>0:
    digit=number%10
    number=number//10
    reverse=reverse*10+digit
    print("reverse of number:",reverse)

   # check if number prime

