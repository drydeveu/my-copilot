import random

vokabeln = {
    "1": {"Deutsch": "Auto", "Englisch": "Car"},
    "2": {"Deutsch": "Haus", "Englisch": "House"},
    "3": {"Deutsch": "Maus", "Englisch": "Mouse"},
    "4": {"Deutsch": "Buch", "Englisch": "Book"},
    "5": {"Deutsch": "Fahrrad", "Englisch": "Bicycle"},
    "6": {"Deutsch": "Computer", "Englisch": "Computer"},
}

def frag_vokabel():
    nummer = random.randint(1, 6)
    eingabe = input("Was heißt " + vokabeln[str(nummer)]["Deutsch"] + " auf Englisch? ")
    if eingabe.lower() == vokabeln[str(nummer)]["Englisch"].lower():
        print("Richtig!")
    else:
        print("Falsch!")
    frag_vokabel()

def main():
    frag_vokabel()

if __name__ == '__main__':
    main()
