class Square:
    def __init__(self, id, up, right, down, left):
        self.id = id
        self.face = 0
        self.sides = []
        self.sides.append([])
        self.sides[0].append(up)
        self.sides[0].append(right)
        self.sides[0].append(down)
        self.sides[0].append(left)

        self.sides.append([])
        self.sides[1].append(int(bin(up)[:1:-1], 2))
        self.sides[1].append(int(bin(left)[:1:-1]))
        self.sides[1].append(int(bin(down)[:1:-1]))
        self.sides[1].append(int(bin(right)[:1:-1]))

    def __str__(self):
        return str(self.getSides())

    def __repr__(self):
        #return str(self.getSides())
        return str(self.id)

    def getId(self):
        return self.id

    # {} => {Retourne la pièce courante}
    def flip(self):
        if self.face == 0:
            self.face = 1
        else:
            self.face = 0

    def getSides(self):
        return self.sides[self.face]

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
        if compatibilty == 0 & compatibilty & 0b01110 == 0: # Peut-etre un pb ici => utiliser le xor pour la 2nd comp (voir compte-rendu)
            return True
        return False
