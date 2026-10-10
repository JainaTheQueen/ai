import time

print("Hello! I am AI Bot. What's your name? : ")
time.sleep(3)

name = input()
time.sleep(3)

print(f"Nice to meet you, {name}!")
time.sleep(3)

print("How are you feeling today? (good/bad) : ")
time.sleep(3)
mood = input().lower()
time.sleep(3)
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")
time.sleep(3)
print(f"It was nice chatting with you {name}. Goodbye!")