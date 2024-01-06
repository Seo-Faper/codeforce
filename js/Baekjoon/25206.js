const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(item=>item.split(' '));
let t = 0; 
let s = 0;
for (let [a, b, c] of input) {

	if (c === "P") continue;
    let score = 0.0;
    if (c !=="F"){
       score = 4 + (65 - c[0].codePointAt())
       score += c[1] === "+" ? 0.5 : 0
    }
  	t += b * score
	s += +b; 
}
console.log(t/s);