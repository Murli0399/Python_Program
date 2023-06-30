def count_vowels(input):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel = 0
    for char in input:
        if char.lower() in vowels:
            vowel += 1

    return vowel

input = "Hello"
vowel = count_vowels(input)
print("Number of vowels:", vowel)
