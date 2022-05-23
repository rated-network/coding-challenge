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

Reading through all of the above is not essential to complete the exercise, but it will help to provide context.

## The Exercise

The purpose of this exercise is to implement a full stack application that will help monitor Lido's validators' performance in the last 7 days.
The following components will be a needed:
- Find Lido's validator public keys from on-chain data (an IP address hosting Geth will be provided; ping Aris for details).
- Find their performance by querying https://api.rated.network/ For for more info, check https://api.rated.network/docs
- Display the information in rudimentary frontend as per the following wireframe.


<img width="440" alt="Screenshot 2022-05-23 at 19 39 23" src="https://user-images.githubusercontent.com/4972825/169867319-e133e3a3-e7eb-472c-8234-a6c6adc4a630.png">

## Implementation Notes

