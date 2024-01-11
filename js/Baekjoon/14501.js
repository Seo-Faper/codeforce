const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const n = Number(input[0])
const arr = input.slice(1).map(e=>e.split(" ").map(Number))

let ans = 0
const recur = (idx, value)=>{
    if(idx >= n){
        if(idx > n)
            return
        ans = Math.max(ans,value)
        return 
    }else{
        recur(idx+arr[idx][0], value+arr[idx][1])
        recur(idx+1, value)
    }

}
recur(0,0)
console.log(ans)