## Context

[Rated](rated.network) offers a solution to the poor contextualization of validator quality. The solution is centered around reputation scores for machines and their operators, starting with the Ethereum Beacon Chain. Rated seeks to embed a large swathe of available information from all layers of a given network, and compress it in an easily legible and generalizable reputation score that can act as an input to human workflows but most importantly, machines (e.g. an API that acts as an input to insurance or derivatives Smart Contracts).

## The Exercise

The purpose of this exercise is to manipulate an Ethereum transaction [dataset](https://github.com/rated-network/coding-challenge/blob/main/ethereum_txs.csv) using Python.

The following resources provide the required background:

- [ETH transaction](https://ethereum.org/en/developers/docs/transactions/)
- [Blockchain Explorer](https://etherscan.io/) 
- [Gas fees](https://ethereum.org/en/developers/docs/gas/)
- [ETH Gas Tracker](https://etherscan.io/gastracker)
- [ETH units](https://gwei.io/)

## Guidelines

This solution should consist of 5 parts:

1. Assuming block length is 13 seconds, compute the approximate execution timestamp of each transaction.
2. Compute the gas cost of each transaction in Gwei (1e-9 ETH).
3. Using [Coingecko's](https://www.coingecko.com/en/api/documentation) API, retrieve the approximate price of ETH at transaction execution time and compute the dollar cost of gas used.
4. Populate a local database with the processed transactions.
5. Using the database in part 4, implement an API endpoint in a framework of your choosing that serves the following:

```
GET /transactions/:hash

{
  "hash": "0xaaaaa",
  "fromAddress": "0x000000",
  "toAddress": "0x000001",
  "blockNumber": 1234,
  "executedAt": "Jul-04-2022 12:02:24 AM +UTC",
  "gasUsed": 12345678,
  "gasCostInDollars": 4.23,
}
```

The solution should adhere to production-like coding standards and should be delivered in a GitHub repo.

Bonus points: `pydantic`, `async/await`, `FastAPI`, `pytest`.

Good luck!
