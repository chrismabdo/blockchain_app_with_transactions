import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, transactions, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.trasnactions = transactions
    #self.trasnactions_count = self.trasnactions.size
    self.previous_hash = previous_hash
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.trasnactions).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
    return sha.hexdigest()

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_transaction = "Hey! I'm block" + str(this_index)
    #this_tranaction_count = this_transaction.size
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_transaction, this_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add))