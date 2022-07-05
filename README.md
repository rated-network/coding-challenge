## Context

[Rated](rated.network) offers a solution to the poor contextualization of validator quality problem. This solution is centered around reputation scores for machines and their operators, starting with the Ethereum Beacon Chain. Rated seeks to embed a large swathe of available information from all layers of a given network, and compress it in an easily legible and generalizable reputation score that can act as an input to human workflows but most importantly, machines (e.g. an API that acts as an input to insurance or derivatives Smart Contracts).

## The Exercise

The purpose of this exercise is to manipulate a dataset containing Ethereum Mainnet transactions.

The following resources provide the required context:

- [ETH transaction](https://ethereum.org/en/developers/docs/transactions/)
- [Blockchain Explorer](https://etherscan.io/) 
- [Gas fees](https://ethereum.org/en/developers/docs/gas/)
- [ETH Gas Tracker](https://etherscan.io/gastracker)
- [ETH units](https://gwei.io/)

## Guidelines

This exercise consists of 4 parts:

1/ Assuming block length is 13 seconds, compute the execution timestamp of each transaction.

2/ Compute the gas cost of each transaction in Gwei (1e-9 ETH).

3/ Using [Etherscan's] API, retrieve the price of ETH at transaction execution time.

4/ For the final question, extract any KPIs you find interesting out of the gas cost results and comment.  


As deliverables, we expect you to give the code used to achieve such results, the modified dataset and the graphs.

Good luck!