#count the number of vowels present in a given sentence
sentence = input("Enter a sentence: ")
vowls=['a','e','i','o','u','A','E','I','O','U']
count=0
for char in sentence:
    if char in vowls:
        count+=1
print("No.of vowels present in given sentence is: ",count)