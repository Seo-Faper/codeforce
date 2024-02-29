const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const N = parseInt(input[0]);
const pos = input.slice(1).map((e) => e.split(" ").map(Number));

let ans = new Array(N).fill(10e9);
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    let distance = [];
    for (let k = 0; k < N; k++) {
      distance.push(
        Number(
          Math.abs(pos[i][0] - pos[k][0]) + Math.abs(pos[j][1] - pos[k][1])
        )
      );
    }
    distance.sort((a, b) => a - b);
    let tmp = 0;
    for (let k = 0; k < N; k++) {
      tmp += distance[k];
      ans[k] = Math.min(ans[k], tmp);
    }
  }
}
console.log(ans.join(" "));
