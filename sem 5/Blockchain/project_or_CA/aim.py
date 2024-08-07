import hashlib
import time
import random

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Block:
    def __init__(self, transactions, previous_hash, validator):
        self.transactions = transactions
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.validator = validator
        self.nonce = 0  # Used for demonstration purposes

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.validator) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.authorities = ["Validator1", "Validator2", "Validator3"]  # Simulated validators

    def create_genesis_block(self):
        return Block([], "0", "Genesis")

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_block(self, validator):
        transactions = self.pending_transactions[:]
        transactions.append(Transaction("Network Reward", validator, 1))
        previous_block = self.chain[-1]
        new_block = Block(transactions, previous_block.calculate_hash(), validator)
        while new_block.calculate_hash()[:self.difficulty] != "0" * self.difficulty:
            new_block.nonce += 1
        self.chain.append(new_block)
        self.pending_transactions = []

    def print_chain(self):
        for block in self.chain:
            print(f"Block Hash: {block.calculate_hash()}")
            print(f"Validator: {block.validator}")
            print(f"Transactions: {block.transactions}")
            print("=" * 20)

# Create blockchain and simulate transactions and mining
blockchain = Blockchain()

# Simulate transactions and mining for a few rounds
for _ in range(3):
    sender = random.choice(blockchain.authorities)
    recipient = random.choice(blockchain.authorities)
    amount = random.randint(1, 10)
    transaction = Transaction(sender, recipient, amount)
    blockchain.add_transaction(transaction)

    validator = random.choice(blockchain.authorities)
    blockchain.mine_block(validator)

blockchain.print_chain()
