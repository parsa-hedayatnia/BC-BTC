import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_trxs = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        # create a new block
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'trxs': self.current_trxs,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        # empty_mempool
        self.current_trxs = []
        # add block to the chain
        self.chain.append(block)
        return block

    def new_trxs(self, sender, recipient, amount):
        # add trx to the mempool
        self.current_trxs.append({'sender': sender, 'recipient': recipient, ' amount': amount})

    @staticmethod
    def hash(block):
        # hashing algorithm
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.new(block_string).hexdigest()

    @property
    def last_block(self):
        # return last block
        pass
