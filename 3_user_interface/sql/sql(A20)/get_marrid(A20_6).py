import random
# برنامه ای بنویسید که به صورت تصادفی هر پسر و دختر با هم ازدواج کنند. مثلا:
# results = [(sajjad, soghra), (abdollah, minoo) , …]
# دقت کنید که یک پسر نمی تواند همزمان با دو دختر ازدواج کند و بالعکس 😐
boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]
def get_mareid(boys, girls):
    result = []
    n = min(len(boys), len(girls))
    for i in range(n):
        family = (random.choice(boys), random.choice(girls))
        boys.remove(family[0])
        girls.remove(family[1])
        result.append(family)
    print(result)
get_mareid(boys,girls)


