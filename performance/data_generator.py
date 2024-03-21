import json
import random
from uuid import uuid4

def generate_data_file(file_path, num_records, duplication_rate=0.1):
    # Seed the random number generator for deterministic output
    random.seed(42)
    accounts = [str(uuid4()) for _ in range(10000)]

    records = []
    for _ in range(num_records):
        record = {
            "account_id": random.choice(accounts),
            "transaction_id": str(uuid4()),
            "amount": random.randint(-5000, 10000)
        }
        records.append(record)

        if random.random() < duplication_rate:
            records.append(record)

    with open(file_path, 'w') as file:
        for record in records:
            file.write(json.dumps(record) + '\n')

file_path = "transactions.json"
num_records = 30000000
duplication_rate = 0.01

generate_data_file(file_path, num_records, duplication_rate)
