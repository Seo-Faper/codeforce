const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const n = parseInt(input[0])
ans = 0
for(let A = 0; A<=n; A++){
    for(let B = 0; B <=n; B++){
        for(let C = 0; C <=n; C++){
            if(A + B + C == n){
                if(C >= B + 2 && A % 2 !== 0 && A*B*C !==0){
                    ans++
                }
            }
        }
    }
}
console.log(ans)