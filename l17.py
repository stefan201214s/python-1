rooms = []
items = []
inGame = True
solution = "4611"
guess = ""
lives = 3
dragon_number = 3
print("bienvenue dans mon escape room.Essayede trouver la sortie. Il y a 4 pièces (0-3).")
while inGame == True and lives != 0:
    room_number = input("Quelle pièce veux-tu visiter?")
    if room_number == "0":
        if "key" in items:
          print("Plus rien à faire dans cette pièce.")
        else:
          print("tu a trouvé la clé") 
          items.append("key")
    elif room_number == "1":
        if "key" in items:
          print("vous ouvrez la porte, et vous trouvez un calcul : 23 x 2")
        else:
           print("La porte est bloquée, il nous faut une clé")
    elif room_number == "2":
        print("Je suis + grand que 10, + petit que 30 et la somme de mes chiffres est 22.Qui suis-je?")
    elif room_number == "3":
        input("Je suis devant la sortie, qui requiert un code. ")
        if guess ==  solution:
           print("Vous avez trouvez le bon code. ")
           inGame = True
        else:
            print("Pas le bon code....")
            lives -= 1
            if lives == 2:
                input("Tu fait expres ou c comment???")
            if lives == 1:
                input(" ta encore rater en sah j'espere vrm que c juste pour me faire stresser")

if inGame == True:
   print("maintenant tu dois decapiter la tete du dragon  avec cette épée claquée!")
   print("Objet: Une épée ta été atribuer")
   print("Quête de victoire: Tue le dragon ou tu a perdu")
   dragon_number = input("Choisis un numero entre (1-4)")
   if dragon_number == "2":
    inGame = True
else:
   inGame = False

if inGame == False:
   print("Bah encore heureux qeta reussis")
else:
   print("t grv eteint lache le jeux, force a tes parent.")

