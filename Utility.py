def reverseBits(num, bitSize):
        binary = bin(num)[2:]
        binary = binary.zfill(bitSize)
        return binary[::-1]