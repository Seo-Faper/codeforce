const Web3 = require('web3');
const web3 = new Web3('http://43.201.150.10:8888/4eb933ef-4f0b-4042-9bed-3574b64edcbd');

web3.eth.getChainId().then(console.log);
