const fs = require("fs");
const data = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const MOD = 1000000007n;

let [N_str, x_str] = data[0].split(" ");
const N = Number(N_str);
const x = BigInt(x_str);

const values = new Array(N + 1);
for (let i = 0; i <= N; i++) {
  const line = data[i + 1];
  const spaceIdx = line.indexOf(" ");
  const valStr = spaceIdx > 0 ? line.substring(0, spaceIdx) : line;
  values[i] = BigInt(valStr);
}

let prev = values[0];
for (let i = 1; i <= N; i++) {
  prev = (prev * x + values[i]) % MOD;
}

console.log(Number(prev));
