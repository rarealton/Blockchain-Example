# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:03:04 2021

@author: alton
"""
import hashlib
import json
from time import time
import pickle

    
class Blockchain():
    
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        
        self.new_block(previous_hash = "The beggining of the end. IDK what else to put but want to add stuff to this message. Thanks for enjoying this code.", proof = 100)
        
  
    #creates a new block pairs in a JSON object. Then resets the list of pending transactions. Adds the newest block to the chain.        
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            }
        
        self.pending_transactions = []
        self.chain.append(block)
        
        return block
    
    
    #Search blockchain for most recent block
    @property
    def last_block(self):
        
        return self.chain[-1]
    
    
    #Add a transaction with relvant info to 'blockpool' -list of pending transactions.
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
            }
        self.pending_transactions.append(transaction)
        
        return self.last_block['index'] + 1
    
    
    #recieve one block. Turn it into string, turn that into Unicode (to hash). Hash with SHA512 encryption, then translate the Unicdoe into a hexidecimal string.
    
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        
        raw_hash = hashlib.sha512(block_string)
        hex_hash = raw_hash.hexdigest()
        
        return hex_hash
    

blockchain = Blockchain()
t1 = blockchain.new_transaction("The chain", "Alton", 5)
t2 = blockchain.new_transaction("The chain", "Bob", 1)
t3 = blockchain.new_transaction("The chain", "John", 5)
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Alton", "Brian", 1)
t5 = blockchain.new_transaction("The chain", "Brian", 2)
t6 = blockchain.new_transaction("John", "Mario", 3)
blockchain.new_block(6789)

print("Genesis block: ", blockchain.chain)      

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(blockchain.chain, f, ensure_ascii=False, indent = 4)
 
    
#hases issues saving data and isn't clean so went with above method instead 
#out_file = open("myBLockChainFile.json", "wb")
#pickle.dump(blockchain.chain, out_file)
#out_file.close()
    
    