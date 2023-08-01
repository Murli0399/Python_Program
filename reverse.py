str = input("Enter word")

def reverse(str):
  s = ''
  for i in str:
    s = i + s
    
  return s

print(reverse(str))
