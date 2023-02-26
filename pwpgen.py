import string
import random

letter = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

A = letter + digits + special_chars

decision = input("Möchten sie ein Passwort generieren [y/n]?: ")

def x():
    pwd = ""
    if decision == "y":
        B = int(input("Anzahl der Elemente: "))
        for i in range(B):
            pwd += "".join(random.choice(A))
        print(pwd)

    else:
        print("Sie haben sich für nein entschieden")

x()
