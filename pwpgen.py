import random

groß_buchstaben = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
klein_buchstaben = ["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
zahlen = range(0,9)
zeichen = ["!","?","§","%"]

A = input("Möchten sie ein Passwort generieren [y/n]?: ")


def x():
    if A == "y":
      print(random.choice(groß_buchstaben),random.choice(klein_buchstaben),random.choice(zahlen),random.choice(zeichen), random.choice(groß_buchstaben),random.choice(klein_buchstaben),random.choice(zahlen),random.choice(zeichen))

    else:
        print("Sie haben sich für nein entschieden")


x()