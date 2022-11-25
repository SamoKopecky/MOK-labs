from datetime import datetime
from typing import NamedTuple, List


class Blockchain:
    block_id = 0
    transaction_id = 0

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def new_block(self, previous_hash=None, difficulty=None):
        pass

    def genesis_block(self):
        self.block_id += 1
        genesis_transaction = Transaction(
            self.transaction_id,
            self.get_timestamp(),
            "",
            "Satoshi",
            50,
        )
        self.chain.append(
            Block(
                self.block_id, self.get_timestamp(), 0, [genesis_transaction], 0, 0, 0
            )
        )

    def new_transaction(self, sender, recipient, amount):
        self.transaction_id += 1
        transaction = Transaction(
            self.transaction_id,
            self.get_timestamp(),
            sender,
            recipient,
            amount,
        )
        self.pending_transactions.append(transaction)
        return self.transaction_id

    def search_transaction(self, transaction_id):
        pass

    @staticmethod
    def get_timestamp():
        return datetime.timestamp(datetime.now())


class Transaction(NamedTuple):
    id: int
    timestamp: float
    sender: str
    recipient: str
    amount: int


class Block(NamedTuple):
    index: int
    timestamp: float
    difficulty: int
    transactions: List[Transaction]
    transactions_hash: int
    previous_hash: int
    nonce: int


def main():
    blockchain = Blockchain()
    blockchain.genesis_block()
    t1 = blockchain.new_transaction("Satoshi", "Mike", 5)
    t2 = blockchain.new_transaction("Mike", "Satoshi", 1)
    blockchain.new_block()


if __name__ == "__main__":
    print("test")
    main()
