import random
while True:
    user_input = input("For rolling the dick press a key :")
    dick = random.randint(1, 6)
    print("🎲 : ", dick)
    if dick == 6:
        print("Great, you can roll it again")
    else:
        break

