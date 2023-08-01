def palindrome(num):
  s = str(num)
  rev = s[::-1]
  if(s == rev):
    return "True"
  else:
    return "False"
  

num = int(input("Enter Number : "))
print(palindrome(num))
