const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const N = Number(input[0]);
let dp = Array(N + 1)
  .fill()
  .map(() => new Array(N + 1).fill(0));
let arr = Array(999999 + 1)
  .fill(true)
  .fill(false, 0, 2);

for (let i = 2; i * i <= 999999; i++) {
  if (arr[i]) {
    for (let j = i * i; j <= 999999; j += i) {
      arr[j] = false;
    }
  }
}
arr[11] = false;

for (let i = 1; i <= N; i++) {
  for (let j = 1; j <= N; j++) {
    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
    let p = Number(i + "" + j);

    dp[i][j] += arr[p] ? 1 : 0;
  }
}
console.log(dp[N][N]);
