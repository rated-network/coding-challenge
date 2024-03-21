## Context

[Rated](rated.network) offers a solution to the poor contextualization of validator quality. The solution is centered around reputation scores for machines and their operators, starting with the Ethereum Beacon Chain. 

Rated seeks to embed a large swathe of available information from all layers of a given network, and compress it in an easily legible and generalizable reputation score that can act as an input to human workflows but most importantly, machines (e.g. an API that acts as an input to insurance or derivatives Smart Contracts).

## The Exercise

This coding exercise is designed to assess your ability to write performant software. You will be working with a large synthetic dataset representing financial transactions, where your task is to efficiently compute the final balance for each account. The dataset will be provided to you in the form of a very large file, where each line is a JSON object containing an account's transaction details.

### Objective

Your primary objective is to develop a program that reads this large dataset and computes the final balance of each account as quickly and efficiently as possible. The dataset contains duplicates, and part of your challenge is to correctly handle these duplicates in your computation.

### Dataset Description

Each line in the dataset file is a JSON object with the following fields:

`account_id`: A unique identifier for the account.
`transaction_id`: A unique identifier for the transaction.
`amount`: The transaction amount. This can be positive (credits) or negative (debits).

For example:

```json
{"account_id": "abc123", "transaction_id": "txn001", "amount": 150}
```


### Generating the Dataset

The dataset file can be generated using the provided Python script. To ensure consistency and fairness, you are not allowed to alter the parameters used for generating the file.

```bash
python generate_dataset.py
```

This will create a file named `transactions.json` in the current directory, containing the dataset you will use for this exercise.

### Requirements

- Your program should read the `transactions.json` file, process the data, and compute the final balance for each account.
- Handle duplicate transactions correctly. Each transaction should only be processed once.
- Optimize your solution for speed and efficiency. Consider the memory usage, especially since the dataset might be too large to fit into memory all at once.
- You may use any Python libraries or tools.


### Submission Guidelines

- Provide your solution as a source code file (or files), along with a README file explaining how to run your program.
- Include any requirements or dependencies needed to run your program in a requirements.txt file.

### Evaluation Criteria

Your submission will be evaluated based on correctness and speed. The seed is hardcoded to have a deterministic output and thus the dataset is fixed.

To qualify "speed" a bit better, on a Macbook Pro M2 (where the evaluation will happen), we will use the following classification:
- God: <1s
- Fast: 1-5s
- Decent: 5-10s
- Borderline: 10-20s
- Slow: 20-50s
- Painfully slow: 50s+

Good luck, and we're looking forward to seeing your optimised solution!