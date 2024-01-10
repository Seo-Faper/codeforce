const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const n = Number(input[0])
const [A,B,C,D] = input[1].split(" ").map(Number)

const arr = input.slice(2).map(e=>e.split(" ").map(Number))
let ans = 9999999999
let ingre = []
let result = ""
let flag = true
const recur = (i,a,b,c,d,price)=>{
    
    if(a >= A && b >= B && c >= C && d >= D){
        flag = false
        if(ans > price){
            ans = price
            result = ingre.join(" ")
        }
    }
    if(i==n)return
    ingre.push(i+1)
    recur(i+1,a+arr[i][0],b+arr[i][1],c+arr[i][2],d+arr[i][3],price+arr[i][4])
    ingre.pop(i+1)
    recur(i+1,a,b,c,d,price)
    
}
recur(0,0,0,0,0,0)
if(flag){
    console.log(-1)
}else{
    console.log(ans)
    console.log(result)
}
