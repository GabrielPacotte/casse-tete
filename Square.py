from Utility import reverseBits

class Square:
    def __init__(self, id, up, right, down, left, face=0):
        self.id = id
        self.face = face
        self.sides = []
        self.sides.append([])
        self.sides[0].append(up)
        self.sides[0].append(right)
        self.sides[0].append(down)
        self.sides[0].append(left)
        self.sides.append([])
        self.sides[1].append(int(reverseBits(up, 5), 2))
        self.sides[1].append(int(reverseBits(left, 5), 2))
        self.sides[1].append(int(reverseBits(down, 5), 2))
        self.sides[1].append(int(reverseBits(right, 5), 2))
        
        # self.sides[1].append(int((bin(up)[2:])[::-1], 2))
        # self.sides[1].append(int((bin(left)[2:])[::-1], 2))
        # self.sides[1].append(int((bin(down)[2:])[::-1], 2))
        # self.sides[1].append(int((bin(right)[2:])[::-1], 2))

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        #return str(self.getSides())
        return str(self.id)

    def __copy__(self):
        return type(self)(self.id, self.sides[0][0],self.sides[0][1],self.sides[0][1],self.sides[0][1], self.face)

    # def copy(self):
    #     return Square(self.id, self.sides[0][0],self.sides[0][1],self.sides[0][1],self.sides[0][1], self.face)

    def getId(self):
        return self.id

    # {} => {Retourne la pièce courante}
    def flip(self):
        self.face = (self.face + 1) % 2

    def getFace(self):
        return self.face

    def setFace(self, f):
        self.face = f

    def getSides(self):
        return self.sides[self.face]

    def getEntireValue(self):
        n = self.getSides()[0]
        i = 1
        while i < 4:
            x = self.getSides()[i] - 16 * (n % 2)
            n = (n << 4) + x
            i += 1
        return n >> 1

    def getCompatibilities(self, orientation, other):
        res = []
        res.append([])
        res[0] = self.getFaceCompatibilities(orientation, other)
        other.flip()
        res.append([])
        res[1] = self.getFaceCompatibilities(orientation, other)
        return res

    def getFaceCompatibilities(self, orientation, other):
        otherOrientation = 0
        res = []
        while otherOrientation < 4:
            if self.areSidesCompatible(orientation, otherOrientation, other):
                res.append(otherOrientation)
            otherOrientation += 1
        return res

    def areSidesCompatible(self, orientation, otherOrientation, other):
        compatibilty = self.getSides()[orientation] & other.getSides()[otherOrientation]
        b1_binVal = format(self.getSides()[orientation], "#07b")
        b2_binVal = format(other.getSides()[otherOrientation], "#07b")
        b1 = int(b1_binVal[3:6], 2)
        b2 = int(b2_binVal[3:6], 2)
        fill = b1 ^ b2
        if compatibilty == 0 and fill == 0b111:
            return True
        return False
