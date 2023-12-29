let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let n = parseInt(input[0]);
let l = input[1].split(' ').map(e=>parseInt(e));

let shottest = 0; // 가장 긴 감소하는 수열의 길이를 구해요
let longest = 0; // 가장 긴 증가하는 수열의 길이를 구해요
let curr = 1;
let durr = 1;
for(let i = 1; i<n; i++){
    if (l[i-1] >= l[i]){
        curr++
     
    }else{
        // 계속 비교하다가 한번이라도 l[i-1] < l[i] 인 경우가 발생한다면
        // 현재 curr과 shottest를 비교해 더 큰 값을 갱신해요.
        shottest = Math.max(curr,shottest);
        curr = 1
    }
    if (l[i-1] <= l[i]){
        durr++
    }else{
        longest = Math.max(durr,longest);
        durr = 1
    }
}
shottest = Math.max(curr,shottest);
longest = Math.max(durr,longest);
if(n==1 || n == 2) longest = n

console.log(Math.max(longest,shottest));