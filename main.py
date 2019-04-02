from morpion import morpion

m = morpion()

m.grille = [["X", "X", "O"],
            ["O", "O", "X"],
            ["X", "O", "X"]]

print(m.matchNul())
print(m.gagnant())
