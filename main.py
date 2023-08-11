import hashlib
import json
import sys
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request


class Blockchain:
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

    def new_trx(self, sender, recipient, amount):
        # add trx to the mempool
        self.current_trxs.append({'sender': sender, 'recipient': recipient, ' amount': amount})
        return self.last_block['index']+1

    @staticmethod
    def hash(block):
        # hashing algorithm
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.new(block_string).hexdigest()

    @property
    def last_block(self):
        # return last block
        return self.chain[-1]

    @staticmethod
    def valid_proof(last_proof , proof):
        #check proof is fine or not try again
        this_proof = f"{proof}{last_proof}".encode()
        this_proof_hash = hashlib.new(this_proof).hexdigest()
        return this_proof_hash[:4] == "0000"

    def proof_of_work(self, last_proof):
        #show that the work is done
        proof = 0
        while self.valid_proof(last_proof , proof) is False:
            proof +=1
        return proof

app = Flask(__name__)
node_id = str(uuid4())
blockchain = Blockchain()

# @app.route('/')
# def home(self):
#     return 'Welcome to the Blockchain App!\n ' \
#             '\tAuthor:parsa-Hedayatnia'

@app.route("/mine", methods=['GET'])
def mine():
        #mine one block
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_trx(sender="0", recipient=node_id, amount=6.25)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof,previous_hash)
    res ={
        'message' : "new Trxs",
        'index' : block['index'],
        'trxs' : block['trxs'],
        'proof' : block['proof'],
        'previous_hash' : block['previous_hash']
        }


    return "I will mine one block"

@app.route('/trxs/new', methods=['POST'])
def new_trx():
    #added new trxs
    values = request.get_json()
    this_block = blockchain.new_trx(values['sender'], values['recipient'], values['amount'])
    res = {'message': f'will be added to block{this_block}'}
    return jsonify(res), 201

@app.route('/chain', methods=['GET'])
def full_chain(self, ):
    #print('ssfsds')
    res = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(res), 200
app.run(host='127.0.0.1', port=5000)


