const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");
const N = Number(input[0]);
const M = Number(input[1]);

let arr_room = new Array(2 * N + 1);
for (let i = 0; i <= 2 * N; i++) {
  if (i % 2 === 0) {
    arr_room[i] = "|";
  } else {
    arr_room[i] = (i + 1) / 2;
  }
}

for (let i = 0; i < M; i++) {
  const [x, y] = input[2 + i].split(" ").map(Number);

  const start = 2 * x;
  const end = 2 * y - 2;

  for (let j = start; j <= end; j += 2) {
    if (arr_room[j] === "|") arr_room[j] = " ";
  }
  //console.log(x, y, arr_room.join(""));
}

const ans = arr_room.filter((e) => e === "|").length;
console.log(ans - 1);
