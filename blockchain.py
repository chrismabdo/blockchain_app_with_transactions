import genesis
import block
import new_block

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print(f"Block {block_to_add.index} has been added to the blockahin!")
    print(f"Hash {block_to_add}\n")