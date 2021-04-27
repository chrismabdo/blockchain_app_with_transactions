import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, transactions, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.trasnactions = transactions
    self.trasnactions_count = trasnactions.size
    self.previous_hash = previous_hash
    self.hash = hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update(str(self.index) +
               str(self.timestamp) +
               str(self.trasnactions) +
               str(self.trasnactions_count) +
               str(self.previous_hash))
    return sha.hexdigest()