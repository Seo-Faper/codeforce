const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
let [N, M] = input[0].split(' ').map(Number)

let ans = input[1].split(' ').map(Number).sort((a, b) => a - b);
let arr = [];
let result = [];
const recur = (number) => {
    if (number === M) {
        result.push(arr.join(' ') + '\n');
        return
    }
    for (let i = 0; i < N; i++) {
        arr.push(ans[i]);
        recur(number + 1);
        arr.pop();
    }
}

recur(0);
console.log(result.join(''));
