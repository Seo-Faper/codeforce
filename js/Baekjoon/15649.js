const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number)

N = input[0]
M = input[1]
let arr = [];
const recur = ((number)=>{
    if(number === M){
        console.log(arr.toString().replaceAll(',',' '));
        return
    }
    for(let i = 1; i<=N; i++){
        if(arr.indexOf(i) !== -1) continue
        arr.push(i)
        recur(number+1)
        arr.pop()
    }
})

recur(0)