class morpion:

    def __init__(self):
        self.grille = [[' ' , ' ' , ' '],[' ' , ' ' , ' '],[' ' , ' ' , ' ']]
    
    def estTerminal(self):
        res = False
        #3 lignes :
        for i in range (3):
            if res == False:
                break
            else :
                res = self.identiqueList(self.grille[i])

        #3 colonnes :
        for i in range (3):
            if res == False:
                break
            else :
                res = self.identiqueList(self.grille[j][i] for j in range(3))

        #2 diagonales :
        if res != False:
            res = self.identiqueList(self.grille[i][i] for i in range(3))
        if res != False:
            res = self.identiqueList(self.grille[i][2-i] for i in range(3))
        return res

        
    def identiqueList(self, liste):
        for i in liste:
            res = liste[0]
            if i != liste[0]:
                res = False
        return res

