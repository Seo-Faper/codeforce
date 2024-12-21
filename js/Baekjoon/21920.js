const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = Number(input[0]);
const A = input[1].split(" ").map(Number);
const X = Number(input[2]);

let gcd = (num1, num2) => {
  while (num2 > 0) {
    let r = num1 % num2;
    num1 = num2;
    num2 = r;
  }
  return num1;
};
ans = 0;
size = 0;
for (let i = 0; i < N; i++) {
  if (gcd(X, A[i]) == 1) {
    ans += A[i];
    size++;
  }
}
console.log(ans / size);
