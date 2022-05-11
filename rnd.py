import random

howmuch = int(input("Wie viele Codes?"))

while howmuch > 0:
    print(random.randint(100000000000000000000, 999999999999999999999))
    howmuch = howmuch - 1