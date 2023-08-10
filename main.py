class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_trxs = []

    def new_blocks(self):
        #create a new block
        pass
    def new_trxs(self):
        #add trx to the mempool
        pass
    @staticmethod
    def hash(block):
        #hashing algorithm
        pass
    @property
    def last_block(self):
        #return last block
        pass
