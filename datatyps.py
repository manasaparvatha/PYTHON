
#change elements in a list
marks=[80,90,75]
marks[1]=95
print(marks)

#add the element to a list
marks=[80,90,60]
marks.append(85)
print(marks)

#remove elements from the list
marks=[75,80,90]
marks.remove(90)
print(marks)

numbers=[10,20,30]
numbers.insert(1,15)
print(numbers)

#extend method
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#clear method
numbers=[20,30,40]
numbers.clear()
print(numbers)

#index methode
numbers=[10,20,30,40]
print(numbers.index(30))

#count method
numbers=[30,40,50,60,70,60,40,58]
print(numbers.count(60))

#sort method
numbers=[10,60,90,20,40,80,]
print(numbers.sort())


numbers=[10,20,30,40]
numbers.reverse()
print(numbers)

#copy method
a=[1,2,3,4]
b=a.copy()
print(b)

numbers=[10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


#touple in python
#touple is a collection of multiple values that is ordered and unchangable 
student=("manasa",98,"python")
print(student[0])

#access value in a tuble
student=("manasa",18,"python")
print(student[0])
print(student[1])
print(student[2])


numbers=(10,20,20,10,40)
print(numbers.count(20))

numbers=(10,20,30,40,20,30)
print(numbers.index(20))

numbers=(10,20,30,40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


numbers=[10,20,30,40,50,60,70,80]
print(numbers[1:7:2])

#average of three number
n1=int(input("enter number:"))
n2=int(input("enter number:"))
n3=int(input("enter number:"))
total=n1+n2+n3
print("total",total)
avg=total/3

Base=int(input("Enter base:"))
Exponent=int(input("Enter exponent:"))
a=Base*Exponent
print(a)

#greterthan comparision
a=int(input("enter a"))
b=int(input("enter b"))
print(a>b)

#equality checker
n1=int(input("enter number"))
n2=int(input("enter number"))
print(n1==n2)

