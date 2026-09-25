#if and else statements
if 20>=18:
   print("elgible:")


   age=18
   if age>=20:
    
    print("elgible")
else:
    print("not elgible")

    marks=98
    if marks<=90:
                  print("elgible")


age=16
if age>=18:
         print("eligible")
else:
          print("not eligible")



marks=50
if  marks>=40:
    print("eligible")
else:    
    print("not eligible")

#if elif else
marks=int(input("enter marks:"))

if marks >=90:
     print("grade a")
elif marks >=75:
    print("grade b")
elif marks >=60:
    print("grade c")  
elif marks >=55: 
    print("grade d") 
else:
    print("fail")

#if statement
number=int(input("enter number:"))
if number % 5 == 0:
    print("divisible by 5")


#temperature checker
    tempetrature=float(input("enter temperature:"))
if temperature > 40:
  print("high tempperature:")


  #odd or even check
  number=int(input("enter number"))
if number % 2 == 0:
  print("even")
else:
    print("odd")



    marks=int(input("enter marks:"))
    if marks >=40:
        print("pass")
    else:
        print("fail")

number = int(input("enter  umber:"))
if number >=0:
    print("positive")
else:
    print("negative")

    
a=int(input("enter number1:"))
b=int(input("enter number2:"))
if a>b:
    print("largest:",a)
elif b>a:
    print("largest:",b)
else:
    print("both are equal")


    number=int(input("enter number:"))
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
         print("zero")

         

a=float(input("enter first number:"))
b=float(input("enter second number:"))
operator=input("enter operator(+,-,*,/):")

if operator == "+":
    print("result:",a+b)
elif operator == "-":
    print("result:",a-b)
elif operator == "*":
    print("result:",a*b)
elif operator == "/":
    if b !=0:
          print("result:",a/b)
    else:
         print("cannot divide by zero")
else:
  print("invalid operator")


#enter user name faster
username=input("enter username:")
password=input("enter password:")
if username == "admin":
    if password == "1234":
        print("login successful")
    else:
      print("wrong password")
else:
     print("wrong username")


balance = float(input("enter balance"))
amount = float(input("enter withdrawal amount"))

if amount > 0:
    if amount <= balance:
        balance = balance-amount
        print("withdrawal successful")
        print("remaining balance:",balance)
    else:
        print("insufficient balance")
else:
    print("invalid amount")




age=int(input("Enter age:"))
test=input("Did you pass the driving test? (yes/no)")
if age >= 18:
    if test == "yes":
        print("License can be issued")
    else:
        print("pass the driving licence")
else:
    print("Not eligible")

                                      
                                      
