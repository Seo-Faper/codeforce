const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const n = parseInt(input[0])
const array = input.slice(1).map(Number)
for(let i = 0 ; i<n; i++){
    for(let j = 2; j<1_000_001; j++){
        if(array[i] % j === 0){
            console.log("NO")
            break
        }
        if(j===1_000_000){
            console.log("YES")
        }
    }
}