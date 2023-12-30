let input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
A = input[0];
P = input[1];
arr = [A];

while(true){
    let value = 0
    for(let i = 0; i<A.length; i++){
        value += Math.pow(A[i],P)
    }
    if(arr.indexOf(String(value)) !== -1){
        console.log(arr.indexOf(String(value)));
        break;
    }else{
        arr.push(String(value));
        A = String(value);
    }
}