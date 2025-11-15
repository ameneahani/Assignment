import gtts
import os
def read_from_file():
    global words_bank
    file = os.listdir("..\Assign8")

    if "translate1.txt" in file:
        f = open("translate1.txt",'r')
        temp = f.read().split("\n")
        f.close()
        words_bank = []
        for i in range(0, len(temp), 2):
            my_dict = {'en': temp[i], 'fa': temp[i+1]} #دیکشنری میسازیم از فارسی و انگلیسی هر کلمه 
            words_bank.append(my_dict) # لیستی از دیکشنری های کوچک
    else:
        print("Database not found !")

def show_menu():
    print("1- tanslate english to farsi")
    print("2- translate farsi to english")
    print("3- add a new word to database")
    print("4- exit")

def translate_eng_to_fa():
    global output
    output = ""
    user_text = input("Enter English text: ")
    user_sentences = user_text.split(".")
    
    for sentence in user_sentences:
        user_words = sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word == word["en"]:
                    output = output + word["fa"] + " "
                    break
            else:
                output = output + user_word + " "
        output = output + "."
    print(output)

def translate_fa_to_eng():
    global output
    output = ""
    user_text = input("Enter your persian text: ")
    user_sentences = user_text.split(".")
    for sentence in user_sentences:
        user_words = sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word == word['fa']:
                    output = output + word['en'] + " "
                    break
            else:
                output = output + user_word + " "
        output = output + "."
    print(output)

def add_to_database():
    word_en = input("Enter the word in english: ")
    word_fa = input("Enter the word in farsi: ")
    my_dict = {'en':word_en, 'fa':word_fa}
    words_bank.append(my_dict)

def write_to_database():
    f = open("translate1.txt",'w')
    for word in words_bank:
        f.write(word['en']+'\n')
        f.write(word['fa']+'\n')
    f.close()

def convert_text_to_voice(language):
    print(language)
    voice = gtts.gTTS(output, lang = language, slow = False)
    voice.save("voice.mp3")


read_from_file()
print("Welcome to my Translator :")
while True:
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1 :
        translate_eng_to_fa()
        convert_text_to_voice("ar")
    elif choice == 2:
        translate_fa_to_eng()
        convert_text_to_voice("en")
    elif choice == 3:
        add_to_database()
    elif choice == 4:
        write_to_database()
        exit(0)
