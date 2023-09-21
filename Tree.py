from Square import Square
from Utility import reverseBits
from copy import deepcopy

lines = []
for i in range(0b11111):
    lines.append(format(i, "#07b")[2:].replace("0", "⬛").replace("1", "🟥"))

class Tree:
    # pattern doit être de la forme:
    # [ (idPiece1, orientation), (idPiece2, orientation), ...]
    # avec orientation le numéro de la face "vers le haut" lorsque le pattern est disposé comme suis :
    #  O
    #  OOOO
    #  O
    def __init__(self, pattern, pieces, newPiece, sideToComplete):
        self.children = []
        self.availablePieces = pieces[:]
        self.pattern = pattern[:]
        self.newPiece = newPiece
        self.sideToComplete = sideToComplete
        rotation = -1
        # if newPiece.getFace() == 0:
        #     rotation = 1
        self.pattern.append((self.newPiece, (sideToComplete+rotation)%4, self.newPiece.getFace()))
        self.availablePieces.remove(newPiece)

    def addChild(self, child):
        self.children.append(child)

    def iterate(self):
        #print(self.pattern, " => ", compatibilities)
        # create new tree nodes
        if len(self.pattern) < 4:
            compatibilities = self.findAllCompatibilities()
            for pieceIndex in compatibilities.keys():
                for facing in compatibilities[pieceIndex]:
                    for side in facing:
                        self.children.append(Tree(self.pattern, self.availablePieces, self.availablePieces[pieceIndex], (side+2)%4))
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
            # reste à positionner les deux dernières pièces...

    def findAllCompatibilities(self):
        res = {}
        #self.newPiece.setFace(self.face)
        for pieceIndex in range(len(self.availablePieces)-1):
            piece = self.availablePieces[pieceIndex]
            res[pieceIndex] = self.newPiece.getCompatibilities(self.sideToComplete, piece)
        return res

    def isLaneValid(self):
        p1 = self.pattern[0][0]
        #p1.setFace(self.pattern[0][2])
        p1_orientation = self.pattern[0][1]
        p1_rotation = -1
        if self.pattern[0][2] == 1:
            p1_rotation = 1
        p4 = self.pattern[3][0]
        p4.setFace(self.pattern[3][2])
        p4_orientation = self.pattern[3][1]
        p2_rotation = 1
        if self.pattern[3][2] == 1:
            p2_rotation = -1
        if p1.areSidesCompatible((p1_orientation+p1_rotation)%4, (p4_orientation+p2_rotation)%4, p4):
            return True
        else:
            return False
        
    def drawPattern(self):
        # Upper Line
        line = ""
        for pieceData in self.pattern:
            pieceData[0].setFace(pieceData[2])
            line += lines[pieceData[0].getSides()[pieceData[1]]] + " "
        print(line)
        # Middle lines

        i=1
        while i<4:
            line = ""
            for pieceData in self.pattern:
                #print(bin(pieceData[0].getSides()[(pieceData[1]-1)%4]))
                val = format(pieceData[0].getSides()[(pieceData[1]-1)%4], "#07b")[2:]
                if val[i] == '1':
                    line += '🟥'
                else:
                    line += '⬛'
                line += "🟥🟥🟥"
                val = pieceData[0].getSides()[(pieceData[1]+1)%4]
                val = reverseBits(val, 5)
                if val[i] == '1':
                    line += '🟥 '
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