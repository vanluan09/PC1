import binascii
from bitstring import BitArray
from PrefixCodeTree import PrefixCodeTree 

class PrefixCodeTree:

    def __init__(self):
        self.right = None
        self.left = None
        self.symbol = None
    def insert(self, codeword, symbol):
        '''insert codeword to a tree'''
        for b in codeword:
            if b == 0:
                if self.left is None: 
                    self.left = PrefixCodeTree()
                self = self.left
            elif b == 1:
                if self.right is None: 
                    self.right = PrefixCodeTree()
                self = self.right
        self.symbol = symbol

    def decode(self, encodedData, datalen):
        encodedDataList = list(BitArray(encodedData).bin)
        node = self 
        decodeData = node.symbol
        for b in range(datalen):
            if encodedDataList[b] == '1': 
                node = node.right
            elif encodedDataList[b] == '0': 
                node = node.left
            if node == None : 
                return "@@@@@"
            elif node.symbol != None: 
                decodeData += node.symbol
                node = self
        return decodeData


codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}
codeTree = PrefixCodeTree()
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)
message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)