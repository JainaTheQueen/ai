import random
destination={
    "beaches":["bali","Ushlanga rocks","Maldives"],
    "mountains":["everest","Table","Pokhara"],
    "cities":["New-york","Botswana","Dubai"]
}
jokes=["What do you call a fake noodle? An impasta","Why don't scientists trust atoms? Because they make up everything","Why did the invisible man quit his job? Because he couldn't see himself doing it"]

def recomend():
    pre=input("enter beaches, mountains or cities")
    if (pre in destination) :
        place = random.choice(destination[pre])
        print("try this",place)
    else:
        print('invalid choice')

def packing():
    days=input("input the no days")
    place=input("enter the place")
    print(f"enjoy the holidays at {place} for these {days}!")

def chat():
    while True:
        msg=input("enter from recomend, packing or joke")
        if "recomend" in msg:
            recomend()
        elif "joke" in msg:
            print(random.choice(jokes))
        elif "packing" in msg:
            packing()
        elif msg in ["exit","bye"]:
            print("Good bye :(")
            break
        else:
            print("enter from recomend, packing or joke")
chat()