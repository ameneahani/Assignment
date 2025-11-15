# counting the number of words in a sentences

sentences = input("Please enter your sentences : ")
word =1
for i in range(len(sentences)):
    if sentences[i] == " ":
        word = word+ 1
print("your sentences have ",word, "words")

