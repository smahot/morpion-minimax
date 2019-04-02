class morpion:

    def __init__(self):
        self.grille = [[' ' for j in range(3)] for i in range(3)]
    
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

    def TerminalTest (self):
        res = True
        for i in range(3):
            if " " in self.grille[i]:
                res = False
        return res
        
    def identiqueList(self, liste):
        for i in liste:
            res = liste[0]
            if i != liste[0]:
                res = False
        return res

    def utility (self):
        return 0
