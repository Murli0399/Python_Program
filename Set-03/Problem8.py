def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
        word_count = len(text.split())

    with open(output_file, 'w') as file:
        file.write(f"Number of words: {word_count}")

input_file = "Set-03\input.txt"
output_file = "Set-03\output.txt"

count_words(input_file, output_file)