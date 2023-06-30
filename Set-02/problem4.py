str1 = "PyNaTive"

lowercase = ""
uppercase = ""

for char in str1:
    if char.islower():
        lowercase += char
    else:
        uppercase += char

arranged_str = lowercase + uppercase

print(arranged_str)
