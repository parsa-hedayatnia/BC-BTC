from datetime import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_trxs = []

    def new_blocks(self,proof,previous_hash=None):
        #create a new block
        block = {
            'index': len(self.chain)+1,
            'timestamp' : time(),
            'trxs' : self.current_trxs,
            'proof' : proof,
            'previous_hash' :previous_hash
        }
    def new_trxs(self,sender,recipient,amount):
        #add trx to the mempool
        self.current_trxs.append({'sender':sender ,'recipient': recipient , ' amount' : amount})
    @staticmethod
    def hash(block):
        #hashing algorithm
        pass
    @property
    def last_block(self):
        #return last block
        pass
