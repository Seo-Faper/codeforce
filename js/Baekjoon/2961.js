const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const n = Number(input[0])
const arr = input.slice(1).map(e=>e.split(" ").map(Number))
let ans = 9999999999

const recur = (idx, sin, ssun,now)=>{
    if(idx==n){
        if(now==0)
            return
        // console.log(sin,ssun)
        let result = Math.abs(sin - ssun)
        ans = Math.min(result,ans)
        return
    }
    recur(idx+1,sin*arr[idx][0],ssun+arr[idx][1],now+1) //신맛과 쓴맛을 고르거나
    recur(idx+1,sin, ssun, now) // 고르지 않거나 
}
recur(0,1,0,0)
console.log(ans)