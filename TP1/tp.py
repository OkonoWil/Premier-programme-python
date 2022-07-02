dico = {"aide" : "Affiche les commandes du programme",
        "surface" : "Calculer la surface en m2",
        "volume" : "Calculer le volume en m3",
        "quitter" : "Quitter le programme"}
print("Tapez 'aide' pour afficher les commandes")
reponse = input("com>")
while reponse != "quitter":
    if(reponse == "aide"):
        print("Liste des commandes du programme")
        print("--------------------------------")
        for key , value in dico.items():
            print(key , ":" , value)
        print("-----------------------------------------")
        reponse = input("com>")
    elif(reponse == "surface"):
        try:
            long = float(input("Longuer ?"))
            larg = float(input("Largueur ?"))
            print(f"La surface est de {long*larg}m2")
        except:
            print("Une erreur s'est produit")
        finally:
            print("-----------------------------------------")
            reponse = input("com>")

    elif(reponse == "volume"):
        try:
            long = float(input("Longuer ?"))
            larg = float(input("Largeur ?"))
            haut = float(input("Hauteur ?"))
            print(f"La surface est de {long*larg*haut}m3dd")
        except:
            print("Une erreur s'est produit")
        finally:
            print("-----------------------------------------")
            reponse = input("com>")
    else:
        print("-----------------------------------------")
        print("Commande non reconnue")
        reponse = input("com>")
print("Au revoir")



        
