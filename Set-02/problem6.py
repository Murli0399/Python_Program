list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = []

for item1 in list1:
    for item2 in list2:
        new_list.append(item1 + item2)

print(new_list)
