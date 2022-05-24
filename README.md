## Coding Challenge

**Reward**: £1,000.00  
**Payment terms**: Payment on completion, via bank transfer in a UK bank account.  
**Solution Delivery**: GitHub repository (if private, add https://github.com/ariskk as a contributor)  

## Context

[Lido](https://lido.fi) is [Ethereum](https://ethereum.org/en/)’s largest liquid staking protocol.   
Ether holders deposit their ether to Lido to help secure the Ethereum blockchain, earn staking rewards and use their staked tokens in various DeFi applications.  
Lido uses that ether to launch validators using a pool of professional operators, those validators earn rewards, Lido and the operators keep a cut and the rest goes back to the depositors.  

For more information:
- Proof of Stake on Ethereum: https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/
- Staking on Ethereum: https://ethereum.org/en/staking/
- A primer on Lido: https://lido.fi/static/Lido:Ethereum-Liquid-Staking.pdf

Reading through all of the above is not essential to complete the exercise, but it will help provide context.

## The Exercise

The purpose of this exercise is to implement a full stack application that will help monitor Lido's validators' performance in the last 7 days.
The following components will be a needed:
- Find Lido's validator public keys from on-chain data (an IP address hosting Geth (Eth1) and Lighthouse (Eth2 - Beacon) will be provided; ping Aris for details).
- Find their performance by querying https://api.rated.network/ For for more info, check https://api.rated.network/docs
- Display the information in a rudimentary frontend as per the following wireframe.

<img width="433" alt="Screenshot 2022-05-24 at 10 05 41" src="https://user-images.githubusercontent.com/4972825/169969562-e5b060f8-b739-4324-9586-1403f4787fe9.png">

Notes:
- The implementations doesn't have to be real-time. It is fine to just write a script that populates SQLite.
- Use whichever language or framework you are comfortable with. 
- Lido runs 120K+ validators. You don't need to fetch all of them. It is fine to fetch a 5K sample.
- Sort validators by effectiveness rating. The implementation should paginate over them.
- You can use off the shelf components (eg https://react-table.tanstack.com/). The wireframe is indicative.

## Implementation Helpers

To fetch Lido's top level stats:
```
curl -X 'GET' \
  'https://api.rated.network/v0/eth/operators/Lido/effectiveness?size=1' \
  -H 'accept: application/json'
```

To fetch a validator's effectiveness for the last 7 days:
```
curl -X 'GET' \
  'https://api.rated.network/v0/eth/validators/10/effectiveness?size=7' \
  -H 'accept: application/json'
```

To find Lido's pubkeys, you either need to call the contract directly using something like [Web3.js](https://web3js.readthedocs.io/en/v1.7.3/getting-started.html):
```ts
const w3 = new Web3(new Web3.providers.WebsocketProvider('ws://18.209.27.197:8546'))
const CONTRACT_ADDRESS = '0x55032650b14df07b85bF18A3a3eC8E0Af2e028d5'
const NODE_OPERATOR_CONTRACT_ABI = [...] // https://github.com/lidofinance/lido-python-sdk/blob/master/lido_sdk/contract/abi/NodeOperatorsRegistry.json
const ops_contract  = new web3.eth.Contract(NODE_OPERATOR_CONTRACT_ABI, CONTRACT_ADDRESS)
// to get the total number of operators from the smart contract
const total_ops = await ops.methods.getNodeOperatorsCount().call() // it is 22
// You could get a 5K sample like that:
[...Array(5000).keys()].map(i => {
  const result = await ops.methods.getSigningKey(i % total_ops, i // total_ops).call()
  return result
})
```
or you could use https://github.com/lidofinance/lido-python-sdk.

Pubkeys can be resolved to validator indices with a single call to the Beacon node.


