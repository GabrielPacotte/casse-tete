from Square import Square

class Tree:
    # pattern doit être de la forme:
    # [ (idPiece1, orientation), (idPiece2, orientation), ...]
    # avec orientation le numéro de la face "vers le haut" lorsque le pattern est disposé comme suis :
    #  O
    #  OOOO
    #  O
    def __init__(self, pattern, pieces, newPiece, sideToComplete):
        self.children = []
        self.availablePieces = pieces.copy()
        self.pattern = pattern.copy()
        self.newPiece = newPiece
        self.sideToComplete = sideToComplete
        self.pattern.append((newPiece, (sideToComplete-1)%4))
        self.availablePieces.remove(newPiece)

    def addChild(self, child):
        self.children.append(child)

    def iterate(self):
        compatibilities = self.findAllCompatibilities()
        #print(self.pattern, " => ", compatibilities)
        # create new tree nodes
        if len(self.pattern) < 4:
            for pieceIndex in compatibilities.keys():
                for face in compatibilities[pieceIndex]:
                    for side in face:
                        self.children.append(Tree(self.pattern, self.availablePieces, self.availablePieces[pieceIndex], (side+2)%4))
            for child in self.children:
                child.iterate()
        # Validation nécessaire entre la première et la dernière pièce posée
        else:
            p1 = self.pattern[0][0]
            p4 = self.pattern[3][0]
            if p1.areSidesCompatible(3, (self.sideToComplete+2)%4, self.newPiece):
                print(self.pattern, " est VALIDE", (self.sideToComplete+2)%4)
            else:
                print(self.pattern, " est INVALIDE")

    def findAllCompatibilities(self):
        res = {}
        for pieceIndex in range(len(self.availablePieces)-1):
            piece = self.availablePieces[pieceIndex]
            res[pieceIndex] = self.newPiece.getCompatibilities(self.sideToComplete, piece)
        return res
