from morpion import morpion

m = morpion()

m.tour = "X"
m.grille = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


print("Début de la partie")

while not (m.gagnant() or m.matchNul()) :
    print(m.display())
    print(m.tour)
    print("Entrez les coordonnées de la case :")
    print("Calcul des actions possibles (peut durer 10s)")
    print(m.MinMax())
    x = int(input("Entrez x:"))
    y = int(input("Entrez y:"))
    m.Results([x,y],m.tour)
    print("changement effectué")
    m.tourSuivant()

print(m.grille)
print("fin du jeu, le gagnant est :")
print(m.gagnant())

