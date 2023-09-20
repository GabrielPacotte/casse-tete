from Square import Square
from Utility import reverseBits
from copy import deepcopy

lines = []
for i in range(0b11111):
    lines.append(format(i, "#07b")[2:].replace("0", "⬛").replace("1", "⬜"))

class Tree:
    # pattern doit être de la forme:
    # [ (idPiece1, orientation), (idPiece2, orientation), ...]
    # avec orientation le numéro de la face "vers le haut" lorsque le pattern est disposé comme suis :
    #  O
    #  OOOO
    #  O
    def __init__(self, pattern, pieces, newPiece, sideToComplete, face=0):
        self.children = []
        self.availablePieces = pieces[:]
        self.pattern = pattern[:]
        self.newPiece = newPiece
        self.sideToComplete = sideToComplete
        rotation = 1
        if newPiece.getFace() == 0:
            rotation = -1
        self.pattern.append((newPiece, (sideToComplete+rotation)%4, newPiece.getFace()))
        self.availablePieces.remove(newPiece)

    def addChild(self, child):
        self.children.append(child)

    def iterate(self):
        #print(self.pattern, " => ", compatibilities)
        # create new tree nodes
        if len(self.pattern) < 4:
            compatibilities = self.findAllCompatibilities()
            for pieceIndex in compatibilities.keys():
                face = 0
                for facing in compatibilities[pieceIndex]:
                    for side in facing:
                        self.children.append(Tree(self.pattern, self.availablePieces, self.availablePieces[pieceIndex], (side+2)%4, face))
                    face += 1
            for child in self.children:
                child.iterate()
        # Validation nécessaire entre la première et la dernière pièce posée sur la ligne de 4
        elif self.isLaneValid():
            # upLine = self.pattern[0][0].getSides()[self.pattern[0][1]]
            # i = 1
            # while i < 4:
            #     n = self.pattern[i][0].getSides()[self.pattern[i][1]] # 0b101 0101 1101 0101
            #     #print(f"ajout de ({self.pattern[i][0]}, {self.pattern[i][1]}) {n}")
            #     upLine = (upLine << 4) + n
            #     i += 1
            print(f"{self.pattern} => ")#{bin(upLine)}")
            self.drawPattern()

    def findAllCompatibilities(self):
        res = {}
        for pieceIndex in range(len(self.availablePieces)-1):
            piece = self.availablePieces[pieceIndex]
            res[pieceIndex] = self.newPiece.getCompatibilities(self.sideToComplete, piece)
        return res

    def isLaneValid(self):
        p1 = self.pattern[0][0]
        p1_orientation = self.pattern[0][1]
        p4 = self.pattern[3][0]
        p4_orientation = self.pattern[3][1]
        if p1.areSidesCompatible((p1_orientation-1)%4, (p4_orientation+1)%4, p4):
            return True
        else:
            return False
        
    def drawPattern(self):
        # Upper Line
        line = ""
        for pieceData in self.pattern:
            line += lines[pieceData[0].getSides()[pieceData[1]]] + " "
        print(line)
        # Middle lines

        i=1
        while i<4:
            line = ""
            for pieceData in self.pattern:
                #print(bin(pieceData[0].getSides()[(pieceData[1]-1)%4]))
                rotation = 1
                if pieceData[0].getFace() == 0:
                    rotation = -1
                val = format(pieceData[0].getSides()[(pieceData[1]+rotation)%4], "#07b")
                if val[i+2] == '1':
                    line += '⬜'
                else:
                    line += '⬛'
                line += "⬜⬜⬜"
                rotation = -1
                if pieceData[0].getFace() == 0:
                    rotation = 1
                val = pieceData[0].getSides()[(pieceData[1]+rotation)%4]
                val = reverseBits(val, 5)
                if val[i] == '1':
                    line += '⬜ '
                else:
                    line += '⬛ '
            print(line)
            i += 1
        # Bottom Line
        line = ""
        for pieceData in self.pattern:
            val = pieceData[0].getSides()[(pieceData[1]+2)%4]
            val = int(reverseBits(val, 5),2)
            line += lines[val] + " "
        print(line)