const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const [N, K] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);
let start = 0;
let end = 0;
let ans = 0;
let seq = Array.from({ length: 100001 }, () => 0);
//console.log(seq);
while (start < N) {
  if (seq[arr[start]] < K) {
    seq[arr[start]]++;
    start++;
  } else {
    seq[arr[end]]--;
    end++;
  }
  //console.log(start, end);
  ans = Math.max(ans, start - end);
}
console.log(ans);
