import hashlib
import time


class Block:
    def _init_(self, index, previous_hash, timestamp, data, validator):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.validator = validator
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = str(self.index) + str(self.previous_hash) + \
            str(self.timestamp) + str(self.data) + str(self.validator)
        return hashlib.sha256(block_data.encode()).hexdigest()


class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]
        self.validators = ["Validator1", "Validator2", "Validator3"]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block", "Genesis Validator")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        if new_block.index == self.get_latest_block().index + 1 and new_block.validator in self.validators:
            if new_block.previous_hash == self.get_latest_block().hash:
                if self.validate_block(new_block):
                    self.chain.append(new_block)
                    print("Block added by", new_block.validator)
                else:
                    print("Block validation failed.")
            else:
                print("Invalid previous hash.")
        else:
            print("Invalid block index or validator.")

    def validate_block(self, block):
        prefix = '0' * self.difficulty
        return block.hash.startswith(prefix)


# Create blockchain instance
blockchain = Blockchain()

# Create new blocks and add them to the blockchain
new_block1 = Block(1, blockchain.get_latest_block().hash,
                   int(time.time()), "Transaction 1", "Validator1")
new_block2 = Block(2, new_block1.hash, int(
    time.time()), "Transaction 2", "Validator2")
new_block3 = Block(3, new_block2.hash, int(
    time.time()), "Transaction 3", "Validator3")

blockchain.add_block(new_block1)
blockchain.add_block(new_block2)
blockchain.add_block(new_block3)

# Print blockchain details
for block in blockchain.chain:
    print("Block Index:", block.index)
    print("Block Validator:", block.validator)
    print("Block Hash:", block.hash)
    print("-" * 20)
