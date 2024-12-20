const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
const S = parseInt(input[0]);
const [Ma, F, Mb] = input[1].split(" ").map(Number);

if (S <= Ma + F + Mb || S <= 240) {
  console.log("high speed rail");
} else {
  console.log("flight");
}
