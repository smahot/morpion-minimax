class morpion:

    def __init__(self):
        self.grille = [[' ' for j in range(3)] for i in range(3)]
    
    def gagnant(self):
        res = False
        #3 lignes :
        for i in range (3):
            if res == False and self.identiqueList(self.grille[i]):
                res = self.grille[i][0]

        #3 colonnes :
        if res == False:
            for i in range (3):
                if res == False and self.identiqueList(self.grille[j][i] for j in range(3)):
                    res = self.grille[0][i]

        #2 diagonales :
        if res == False and self.identiqueList(self.grille[i][i] for i in range(3)):
            res = self.grille[0][0]
        if res == False and self.identiqueList(self.grille[i][2-i] for i in range(3)):
            res = self.grille[2][2]
        return res

    def matchNul (self):
        res = True
        if self.gagnant() == "X" or self.gagnant() == "O":
            res = False
        for i in range(3):
            if " " in self.grille[i]:
                res = False
        return res
        
    def identiqueList(self, liste):
        liste = list(liste)
        res = True
        for i in liste:
            if i != liste[0]:
                res = False

        if res == True:
            return True
        return res

    def utility (self):
        if self.matchNul():
            return 0
        if self.gagnant() == "X":
            return 1
        elif self.gagnant() == "O":
            return -1
        else :
            print("error")
            return False
