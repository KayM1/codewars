# Ter info, ik heb reeds ervaring met het schrijven van oa. webcrawlers, grafische toepassingen (zoals maze solvers) of zelfs games in pygame met python
# Daarom dat ik ook even geprobeerd heb aan wat input controle te doen in deze opdracht
# Het was wel even wat heropfrissen... :-)

import os
import platform
import time

def ispriem(x):
    if x < 2:
        return False
    for i in range(2, int(int(x ** 0.5) + 1)):
        if x % i == 0:
            return False
    return True

def eersteNpriem(n):
    count = 0
    num = 2
    while count < n:
        if ispriem(num):
            count += 1
            print(f"{count}e priemgetal: {num}")
        num += 1

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def slaapje(c,tijd):
    for _ in range(tijd):
        time.sleep(1)
        print(c, end='', flush=True) # print ... op de huidige lijn

def main():
    while True:
        clear()
        print("\nMaak een keuze:")
        print("1. Controleer of een getal een priemgetal is.")
        print("2. Print de eerste N priemgetallen.")
        keuze = input("Voer je keuze in (1 of 2):")

        if keuze == "1":
            try:
                x = int(input("\n 1. Voer een getal in om te controleren of het een priemgetal is: "))
                if ispriem(x):
                    print(f"\n{x} is WEL een priemgetal.")
                else:
                    print(f"\n{x} is GEEN priemgetal.")
            except ValueError:
                print("Ongeldige input. Voer enkel positieve gehele geetallen in.")
            slaapje('',1)
            invalid = False

        elif keuze == "2":
            try:
                n = int(input("\n 2. Geef het aantal priemgetallen dat je wilt zien: "))
                if n > 0:
                    eersteNpriem(n)
                else:
                    print("Voer een positief geheel getal in.")
            except ValueError:
                print("Ongeldige invoer. Voer een geldig geheel getal in.")
            slaapje('',1)
            invalid = False
        
        else:
            print("Ongeldige keuze. Kies 1 of 2. Even geduld we proberen opnieuw.", end = '', flush=True)
            slaapje('.',4)
            invalid = True

        if invalid != True:
            repeat = input('\nWil je opnieuw kiezen? Y/N: ').lower()
            if repeat != 'y' and repeat != 'j' and repeat != 'ja' and repeat != 'yes':
                break
main()
