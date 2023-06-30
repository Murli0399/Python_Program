def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]

data = {}

print(data) 
add_name_age(data, "John", 25)

update_age(data, "John", 26)
print(data) 

delete_name(data, "John")
print(data) 
