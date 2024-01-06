const input = require('fs').readFileSync('js/example.txt').toString().trim().split('\n')
let n = input[0]
let arr = input[1].split(' ').map(Number)
let keyArray = input[1].split(' ').map(Number).sort((a,b)=>a - b)

let idx = 0;
let last = keyArray.toString();

const permutation = (p, rests) =>{
    if(rests.length===0){
       if(p.toString() === arr.toString()){
            if(last === keyArray.toString()){
                console.log(-1)
            }else{
                console.log(last.split(',').join(' '))
            }
            return 0;
        }
       last = p.toString()
    }else{
        rests.forEach((v,idx) => {
            const rest = [...rests.slice(0,idx) , ...rests.slice(idx+1)];
            return permutation([...p,v], rest)
        });
    }
}

permutation([],keyArray)
