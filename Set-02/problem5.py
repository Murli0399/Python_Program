list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

min_len = min(len(list1), len(list2))

for i in range(min_len):
    new_list.append(list1[i] + list2[i])

new_list.extend(list1[min_len:])
new_list.extend(list2[min_len:])

print(new_list)
