from Tree import Tree
from Square import Square

def findAllCompatibilities(currentPiece, orientation):
    res = {}
    for piece in availablePieces:
        res[piece.getId()] = currentPiece.getCompatibilities(orientation, piece)
    return res

allPieces = [
    Square(1, 0b11011, 0b10100, 0b01010, 0b00101),
    Square(2, 0b00101, 0b11011, 0b11010, 0b00100),
    Square(3, 0b11010, 0b01010, 0b01010, 0b00101),
    Square(4, 0b10100, 0b01011, 0b10100, 0b01011),
    Square(5, 0b11010, 0b00100, 0b00100, 0b00101),
    Square(6, 0b01010, 0b00100, 0b01010, 0b00100)
]
availablePieces = allPieces.copy()

#print(findAllCompatibilities(allPieces[0], 0))
#allPieces[2].flip()
root = Tree([], allPieces, allPieces[0], 0)
#root.pattern = [(allPieces[2], 0, 0)]
#root.drawPattern()
#print(allPieces[0].getEntireValue())
root.iterate() 
# 0b1101 1010 0101 00101                                                                                                                                  

# ⬛⬛⬜⬛⬜ 
# ⬛⬜⬜⬜⬜ 
# ⬜⬜⬜⬜⬛ 
# ⬛⬜⬜⬜⬜ 
# ⬛⬛⬜⬛⬛