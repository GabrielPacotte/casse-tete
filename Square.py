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
        #self.sides[1].append(left)
        self.sides[1].append(int(reverseBits(down, 5), 2))
        self.sides[1].append(right)

        #self.sides[1].append(int(reverseBits(right, 5), 2))
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

    def copy(self):
        return Square(self.id, self.sides[0][0],self.sides[0][1],self.sides[0][2],self.sides[0][3], 0)

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
        other.flip()
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
        # a = self.getSides()[orientation]
        # b = other.getSides()[otherOrientation]
        # if a ^ b == 0b11111:
        #     print("(", self, orientation, self.face, ")", "(", other, orientation, other.face, ")", bin(a), bin(b))
        #     return True
        # return False
        #b1_binVal = format(self.getSides()[orientation], "#07b")[2:]
        b1_binVal = reverseBits(self.getSides()[orientation], 5)
        b2_binVal = format(other.getSides()[otherOrientation], "#07b")[2:]
        compatibilty = int(b1_binVal,2) & int(b2_binVal,2)
        b1 = int(b1_binVal[1:4], 2)
        b2 = int(b2_binVal[1:4], 2)
        fill = b1 ^ b2
        if compatibilty == 0 and fill == 0b111:
            print(f"{self, orientation, self.face} = {b1_binVal}") 
            print(f"{other, otherOrientation, other.face} = {b2_binVal, bin(other.getSides()[otherOrientation])[2:]} ")
            print("compatibility = ", compatibilty)
            print("fill = ", fill)
            return True
        return False
