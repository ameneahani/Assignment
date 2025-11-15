#Hang man game
import random
print("Welcom to Hang man game ")
word_bank = ["woman", "man", "child", "school", "tree", "bird", "sound", "flower", "computer", "clock", "python"]

mistake = 0
true_chars = []

computer_word = random.choice(word_bank)

while mistake < 6 :
    true_char =0
    for i in range(len(computer_word)):
        if computer_word[i] in true_chars:
            print(computer_word[i], end= " ")
            true_char += 1
        else:
            print("-", end= " ")

    if len(computer_word) == true_char:
        print("  👏 You Win👏") 
        break


    user_char = input("  ➡️  ➡️  Please enter your character :")
    if len(user_char) == 1:
        user_char = user_char.lower()
        if user_char in computer_word:
            print("✅")
            true_chars.append(user_char)

        else:
            print("❌")
            mistake += 1
            print(mistake)
    else :
        print("Please enter a correct character")

if mistake == 6:
    print("Game Over")




