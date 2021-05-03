import chain


class Block(object):
    def __init__(self, index, previousHash, timestamp, data):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.hash = chain.calculateHash(self)


    def mineBlock(self, difficulty):
        zeros = chain.repeat("0", difficulty)
        self.nonce = 0
        while self.hash[0:difficulty] != zeros:
            self.nonce += 1
            self.hash = chain.calculateHash(self)