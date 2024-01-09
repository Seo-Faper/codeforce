const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
N = Number(input[0].split(' ')[0])
M = Number(input[0].split(' ')[1])

let ans = input[1].split(' ').map(Number).sort((a, b) => a - b);
let arr = [];
const recur = ((number) => {
    if (number === M) {
        console.log(arr.map(i=>ans[i]).toString().replaceAll(',', ' '));
        return
    }
    for (let i = 0; i < N; i++) {
        if (arr.indexOf(i) !== -1 || arr.at(-1) > i) continue
        arr.push(i)
        recur(number + 1)
        arr.pop()
    }
})

recur(0)