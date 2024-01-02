function distance(x1,y1, x2,y2){
    return Math.sqrt(Math.pow((x1-x2),2) + Math.pow((y1-y2),2))
}
function ccw(x1,y1,x2,y2,x3,y3){
    const num1 = (y3 - y1) * (x2 - x1);
    const num2 = (y2 - y1) * (x3 - x1);
    return num1 == num2
}
let p = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
let A = distance(p[0],p[1],p[2],p[3]);
let B = distance(p[2],p[3],p[4],p[5]);
let C = distance(p[0],p[1],p[4],p[5]);

let lines = [A,B,C].sort((a,b)=>a-b);

if (
    (p[0] - p[2]) * (p[3] - p[5]) ===
    (p[2] - p[4]) * (p[1] - p[3])
  )
    console.log(-1);
  else if (
    (!(p[0] - p[2]) && !(p[2] - p[4])) ||
    (!(p[1] - p[3]) && !(p[3] - p[5]))
  )
    console.log(-1);
else if(!ccw(p[0],p[1],p[2],p[3],p[4],p[5])){
    let ans = [2 * A + 2 * B, 2* A + 2 * C, 2*B + 2*C].sort((a, b) => a - b);
    console.log(ans[2] - ans [0]);
}else{
    console.log("-1.0")
}
