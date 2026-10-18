#basic function
def greet():
    print("hello")
    print("welcome to python")
    greet()

#functions without parameter
def welcome():
    print("welcom to python")
welcome()

#functions with perameter
def greet(name):
    print("hello",name)
greet("manasa")
greet(nymi)

#add two numbers
def add(a,b):
    print("sum:",a+b)
add(10,20)
add(50,30)


#function with return value
def add(a,b):
    return a+b
result=add(10,20) 
print(result)


#multiple parameter
def add(a,b):
    print("sum:",a+b)
add(10,20)
add(50,30)

#functions with return values
def add(a,b):
    return a+b
    result=add(5,10)
    print(result)
    if result>10:
        print("result is result is grater than 10")
#function for even or odd
def even_odd(num):
     if num%2 == 0
print("even")
    else:
        print("odd")
        return num%==0
result=even_odd(5)
print(result)
#functions for largest of two numbers
def largest_of_two(a,b):
    if a>b:
        return a
    else:
        return b
result=largest_of_two(5,10)
print(result)
#function with largest three number
def iargest_of_three(a,b,c):
    if a>c:
        return a
     elif b>c:
        return b
    else:
        return c
result=largest_of_three(5,10,15)
print(result)


#functon +user input
def square(number):
    return number*number 
    number=int(input("enter number:"))
result=square(number)
print("square:",result)
#sum of two number given by the user
def add(a,b):
    return a+b
  a=int(input("enter first number:"))
  b=int(input("enter second number:"))
  result=add(a,b)
  print("sum",result)

#even or odd user input
 def even_odd(num):
    if num%2==0:
        return "even"
     else:
        return "odd"
num=int(input("enter number"))
result=even_odd(num)
print(result) 

#largest of three numbers user input
def largest_of_three(a,b,c):
    if a>=b and a>=c:
        return a
     elif b>=c and b>=a:
        return b   
    else:
        returnc
a=int(input("enter first number:"))
b=int(input("enter second number:"))        
c=int(input("enter third number:"))
result=largest_of_three(a,b,c)
print(result)


#great caluclation
def find_great(marks):
    if marks >=90:
        return "A"
    elif marks >=80:
        return "B"   
    elif marks >=70:
        return "C"
    elif marks >=60:
        return "D"
    elif marks >=50:
        return "E"
    else:  
        return "Fail"  
 a=int(input("enter marks:"))
 print("gread=",find_gread(m))       


 #functions+loop
 def multiplication table(number):
    for i in range(1,11):
        print(number ,"X","=",number*i)
number=int(input("enter number:"))
result=multiplication_table(number)
print(result)

#functions with sum of 1 to n
def sum_of_n(n):
    sum=0
    for i in range(1,n+1)
        total+=1
    return total
n=int(input("enter n:"))
print("sum=",sum n(n))
#positive and negative number
def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

n = int(input("Enter a number: "))
check_number(n)

#factorial of number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
#sum of digits
total=0
while n>0
       digit=n%10
       total=total+digit
       n=n//10
       num = int(input("Enter a number: "))
     print("sum of digits:",total)

     #palindro check
     def is_palindrome(s):
        original=s
        reverse=0
        while s>0:
        digit=s%10
        reverse=reverse*10+digit
        s//=10
        if original==reverse:
            return True
         else:
            return False
     num = int(input("Enter a number: "))
     if is_palindrome(num):
        print("palindrome")
    else:
        print("not palindrome") 

#write a program to print the sum of n numbers using the recurtion.
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = int(input("Enter a number: "))
print("Sum =", sum_n(n))

#fibinoci series (1,2,3,4,5,6,7,8)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fib(i), end=" ")





def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def floordiv(a, b):
    return a // b

def power(a, b):
    return a ** b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", add(a, b))
print("Subtraction =", sub(a, b))
print("Multiplication =", mul(a, b))
print("Division =", div(a, b))
print("Modulus =", mod(a, b))
print("Floor Division =", floordiv(a, b))
print("Power =", power(a, b))

#functional scope
c=30
def add():
    a=10
    b=20
    print(a+b+c)
    add()
    