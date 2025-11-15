import random

def palam_polom_game(hand):
    global score_cpu
    global score_human
    cpu_1 = random.choice(["✋", "🤚"])
    cpu_2 = random.choice(["✋", "🤚"])
    if hand == cpu_1 and cpu_1 == cpu_2:
        print(f"computer_1 = {cpu_1}\tcomputer_2 = {cpu_2}\t you = {hand} -→ Equal")
    elif hand == cpu_2 and cpu_1 != cpu_2:
        score_cpu += 1
        print(f"computer_1 = {cpu_1}\tcomputer_2 = {cpu_2}\t you = {hand} -→ computer")
    elif cpu_2 == cpu_1 and cpu_1 != hand:
        score_human += 1
        print(f"computer_1 = {cpu_1}\tcomputer_2 = {cpu_2}\t you = {hand} -→ you")

score_human = 0
score_cpu = 0
hand = 0
for i in range(5):
    human_hand = int(input("please enter your choice: 1- ✋, 2-🤚 :"))
    if human_hand == 1:
        hand = "✋"
    elif human_hand == 2:
        hand = "🤚" 
    palam_polom_game(hand)
if score_cpu > score_human:
    print(f"Computer Win, computer score = {score_cpu}, human score = {score_human}")
elif score_cpu < score_human :
    print(f"Congrajulation you Win, computer score = {score_cpu}, human score = {score_human}")
else:
    print("Equal")
