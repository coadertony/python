import hashlib
import json
import time


class Block:

  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.nonce = 0
    self.hash = self.calculate_hash()

  def calculate_hash(self):
    # Pack all block properties into a sorted string
    block_string = json.dumps(
        {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        },
        sort_keys=True,
    )
    # Return the SHA-256 cryptographic hash
    return hashlib.sha256(block_string.encode()).hexdigest()

  def mine_block(self, difficulty):
    # Require the hash to start with 'difficulty' number of zeros
    target = "0" * difficulty
    while not self.hash.startswith(target):
      self.nonce += 1
      self.hash = self.calculate_hash()

    print(f"  [+] Block #{self.index} mined! Nonce used: {self.nonce}")
    print(f"      Hash: {self.hash}")


class Blockchain:

  def __init__(self):
    self.chain = [self.create_genesis_block()]
    self.difficulty = 3  # Requiring 3 leading zeros

  def create_genesis_block(self):
    return Block(0, time.time(), "Genesis Block (Anchor)", "0")

  def get_latest_block(self):
    return self.chain[-1]

  def add_block(self, new_block):
    new_block.previous_hash = self.get_latest_block().hash
    new_block.mine_block(self.difficulty)
    self.chain.append(new_block)

  def is_chain_valid(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i - 1]

      # 1. Did the data inside this block get tampered with?
      if current.hash != current.calculate_hash():
        return False

      # 2. Does this block point to the correct previous block?
      if current.previous_hash != previous.hash:
        return False

    return True


# ==========================================
# RUNNING THE SIMULATION ON YOUR MACHINE
# ==========================================
if __name__ == "__main__":
  my_crypto = Blockchain()

  print("Mining Block 1...")
  my_crypto.add_block(
      Block(1, time.time(), {"sender": "Alice", "receiver": "Bob", "amount": 50}, "")
  )

  print("Mining Block 2...")
  my_crypto.add_block(
      Block(
          2, time.time(), {"sender": "Bob", "receiver": "Charlie", "amount": 15}, ""
      )
  )

  print(f"\nIs ledger valid right now? --> {my_crypto.is_chain_valid()}")

  # HACKER ATTEMPT: Let's secretly give Alice 9,000 coins in Block 1
  print("\n⚠️ Simulating hacker altering Block #1 data...")
  my_crypto.chain[1].data["amount"] = 9000

  print(f"Is ledger valid after tamper? --> {my_crypto.is_chain_valid()}")