#display personal details using variable
#name=input("enter your name")
#age=int(input("enter your age"))
#height=float(input("enter your height"))
#print(name)
#print(age)
#print(height)


#personalized greeting 
#name=input("enter your name")
#print(F"Hello,{name}!")


#add two numbers read as string
#a=input("enter your numder:")
#b=input("enter your number:")
#a=int(a)
#b=int(b)
#total=a+b
#print("total:",total)

#float to integer conversion
#n=float(input("enter number:"))
#print(n)
#new=int(n)
#print(new)

#sum using arthemetic operator
#a=int(input("enter number:"))
#b=int(input("enter number:"))
#print(a+b)

#length=float(input("enter length:"))
#breadth=float(input("enter breadth:"))
#area=length*breadth
#print(area)


#quotient and remainder
#a=int(input("enter number"))
#b=int(input("enter number"))
#q=a/b
#r=a%b
#print(q)
#print(r)

#power calculation
#base=int(input("enter base"))
#exponent=int(input("enter exponent"))
#total=base**exponent
#print(total)


#grater than comparison
#a=int(input("enter number"))
#b=int(input("enter number"))
#print(a>b)

#equality check
#n1=int(input("enter number"))
#n2=int(input("enter number"))
#print(n1==n2)

#both number positive check
#n1=int(input("enter number"))
#n2=int(input("enter number"))
#print(n1>0 and n2>0)


#at least one even number
#n1=int(input("enter number"))
#n2=int(input("enter number"))
#print(n1%2==0 or n2%2==0)

#logical not on a condition
#num=int(input("enter num"))
#print(not(num>0))

#augmented assighnment operations
#a=int(input("enter a"))
#a=a+5 #a=20+5-->25
#a=a*2 # a=25*2-->20
#a=a-3 #a=50-3-->47
#print(a)


#exchange values of two variables
a=int(input("enter a number"))
b=int(input("enter a number"))
print(a+b)
print(a-b)


#caluclate simple interest
principal=float(input("enter principal"))
rate=float(input("enter rate"))
time=float(input("enter time"))
si=(principal*rate*time)/100
print(si)

#temperature conversion
c=float(input("enter c"))
f=(c*9/5)+32
print(f)

#check divisibility by 3 and 5
n=int(input("enter n"))
print(n%3==0 and n%5==0)


#sum of digits of a two digit number
num=int(input("enter num"))
tens=num//10
units=num%10
total=tens+units
print(total)
