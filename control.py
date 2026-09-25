#check the number is prime
number=int(input("enter number:"))
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
if count == 2:
    print("prime number")
else:
    print("not a prime number:")   



#print all prime number b/w 2 to 100
for number in range(2,101):
    count=0
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
    if count == 2:
        print(number)


    
#break statement
    for i in range(1,11):
        if i==5:
            break 
        print(i)
 #continue statement
for i in range(1,11):
    if i==5:
        continue
    print(i)    


#PASS KEYWORD
for i in range(1,11):
    if i==5:
        pass
    print(i)
#eligible ane not eligible
  #  age=in(input("enter age:"))
  #  if age>=18:
  #     print("Eligible for vote")
  #  else:
  #      print("Not elgible for vote")
        


#print odd numbers from 1 to 10
for i in range(1,11):
    if i % 2==0:
       continue
print(i)


#print numbers  until user enters0 
  while true:
    number=int(input("enetr number"))
    if number==o:
        breakprint("you entered:",number)

#print number from 1 to 100,but skip multiples of 3 and stop at 50
for i in range(1,101):
    if i==50:
        break
    if i %3==0:
        continue
    print(i)

#calculate the sum of positive numbers entered by the user
total=0
while true:
    number=int(input("enter number:"))
    if number <0:
        continue
    if number==0:
        break
    total=total+number
    print("total:",total)

    for i in range(1,101):
        if i % 3 ==0:
            print("first number:",i)
        break


total = 0
for i in rang(10):
    number=int(input("enter number:"))
    if number <0:
        continue
    total=tptal+number
    print("total:",total)

#password check with limited attempts
    correct_password="python234"
    for attempt in range(1,4):
        password=input("enter password")
    if password==correct_password:
        print("login successful")
        break
        print("wrong password")
    else:
            print("account locked")  


 #find the largest number among 5 numbers enterd by the user
    largest=None        
for i in range(5):
    number=int(input("enter number:"))
    if largest is none or number > largest:
        largest=number
        print("largest:",largest)


    smalest=None        
for i in range(5):
    smalest=int(input("enter number:"))
    if largest is none or number < smalest:
        largest=number
        print("smalest:",smalest)