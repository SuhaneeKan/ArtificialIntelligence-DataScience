import hashlib
import time

# Simulated list of validators
validators = ['Validator1', 'Validator2', 'Validator3']

# Simulated blockchain
blockchain = []

# Function to create a new block
def create_block(transactions, previous_block_hash, validator):
    timestamp = time.time()
    block_data = {
        'timestamp': timestamp,
        'transactions': transactions,
        'previous_block_hash': previous_block_hash,
        'validator': validator
    }
    return block_data

# Function to validate a block's integrity
def validate_block(block):
    # Simulated validation logic (e.g., checking timestamp, hash)
    return True

# Simulated transaction data
transactions = [
    {'sender': 'Alice', 'receiver': 'Bob', 'amount': 10},
    {'sender': 'Bob', 'receiver': 'Charlie', 'amount': 5},
    # ... add more transactions
]

# Genesis block
genesis_block = create_block(transactions=[], previous_block_hash='0', validator=validators[0])
genesis_block['hash'] = hashlib.sha256(str(genesis_block).encode()).hexdigest()
blockchain.append(genesis_block)

# Simulate block creation and validation
for i in range(1, 6):  # Create and validate 5 blocks
    transactions = [
        {'sender': 'Alice', 'receiver': 'Bob', 'amount': 5},
        {'sender': 'Bob', 'receiver': 'Charlie', 'amount': 2},
        # ... add more transactions
    ]
    previous_block = blockchain[-1]
    validator = validators[i % len(validators)]  # Rotate validators

    new_block = create_block(transactions, previous_block['hash'], validator)
    new_block['hash'] = hashlib.sha256(str(new_block).encode()).hexdigest()

    if validate_block(new_block):
        blockchain.append(new_block)
        print(f"Block {i} created and validated by {validator}")
    else:
        print(f"Block {i} validation failed")

    time.sleep(1)  # Simulate block creation time

# Print the final blockchain
for block in blockchain:
    print(block)
