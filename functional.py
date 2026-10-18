# global to functional scope
c=30
def add():
    a=10
    b=20
    print(a+b+c)
add()
#functional to global
name="manas"
def disply():
     name="manasa"
     id=100
     print(name)
     print(id)
disply()
print(name)
print(id)


sname="parvatha"
a=20
print(id(a))
sname="parvatha"
def sd():
    global sid
    sid=247
    global location
    location="kadiri"
    print(sid)
    print(location)
    print(sname)
sd()

