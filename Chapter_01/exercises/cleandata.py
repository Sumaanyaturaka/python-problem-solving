#trim whitespace , standardize case , split words
user_input = input("Enter a sentence: ")
words_list = user_input.split()
clean_text = " ".join(words_list)
standardized_text = clean_text.lower()
print(standardized_text)
