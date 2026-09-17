#key values
std={'name':'Manasa','age':'18', 'course':'aiml'}
print(std)

#access elements in dictionary
print(std["name"])
print(std["age"])
print(std["course"])

#change values in dictionary
std["age"]=11
print(std["age"])

#add new data
std["city"]="vijayawada"
print(std)

#remove data
std.pop("city")
print(std)

#get method in dictionary
print(std.get("name"))
#get()returns the value of the specified key
print(std.update({'age':18}))
#set dificult () methode in a dictionary


#popitem () removes the last inserted key value pair
std={"name":"manasa","age":21,"course":"python"}
std.popitem()
print(std)

std={"name":"manasa"}
std.setdefault("age",21)
print(std)

#clear method
std.clear()
print(std)

#copy method
std={"name":"manasa","age":21}
new_std=std.copy()
print(new_std)

#order of evaluation
result=2+13*2
print(result)
