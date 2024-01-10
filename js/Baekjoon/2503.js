const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const n = Number(input[0])
const hints = input.slice(1)
const visit = Array(10).fill(0)
let result = []
const strike = (a, b) => {
    let cnt = 0;
    for (let i = 0; i < a.length; i++) {
        if (a[i] === b[i]) cnt++
    }
    return cnt;
}

const ball = (a, b) => {
    let cnt = 0;
    for (let i = 0; i < a.length; i++) {
       if(a[i]!==b[i] && b.indexOf(a[i]) !== -1 )cnt++
    }
    return cnt;
}
function backtrack(number, visit) {
    if (number.length === 3) {
        
        let flag = true
        let ans = number.join("")
        
        for (let i = 0; i<n; i++) {
            let [num,s,b] = hints[i].split(" ")
            const hits = num.toString();
            if (strike(hits, ans) !== Number(s)) {
                flag = false
                break
            }
            if (ball(hits, ans) !== Number(b)) {
                flag = false
                break
            }
        }
        if (flag) {
            result.push(ans)
            return
        }

    }
    for (let i = 1; i <= 9; i++) {
        if (!visit[i]) {
            visit[i] = true;
            number.push(i)
            backtrack(number, visit)
            number.pop()
            visit[i] = false;
        }
    }
}

backtrack([], visit)
console.log(result.length)
