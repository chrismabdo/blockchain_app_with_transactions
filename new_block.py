def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_transaction = "Hey! I'm block" + str(this_index)
    this_tranaction_count = this_transaction.size
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)