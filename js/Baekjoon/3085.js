function calc(arr, x,y){

    let lineX = 0
    let lineY = 0
    for(let i = x; i<n; i++){
        if(arr[i][y] == arr[x][y]){
            lineX++
        }else break
    }
    for(let i = y; i<n; i++){
        if(arr[x][i]==arr[x][y]){
            lineY++;
        }else break
    }
    return Math.max(lineX, lineY);
}

let p = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const n = parseInt(p[0]);
let arr = new Array(n);
for(let i = 0; i<n; i++){
    p[i+1] = p[i+1].replace('\r','')
    arr[i] = [...p[i+1]]
}
let arrY = Array.from(Array(5), () => Array(2).fill(''))
for(let i = 0; i<n; i++){
    for(let j = 0; j<n; j++){
        arrY[i][j] = arr[i][j]
    }
}
let ans = 0;
for(let x = 0; x < n; x++){
    for(let y = 0; y<n; y++){
        ans = Math.max(ans,calc(arr,x,y))
    }
}
for(let i = 0; i<n-1; i++){
    for(let j = 0; j<n; j++){
        let tmp = arr[i+1][j]
        arr[i+1][j] = arr[i][j]
        arr[i][j] = tmp // 인접한 x축을 바꾼 후 계산 
        for(let x = 0; x < n; x++){
            for(let y = 0; y<n; y++){
                ans = Math.max(ans,calc(arr,x,y))
            }
        }
        
        for(let x = 0; x < n; x++){
            for(let y = 0; y<n; y++){
                arr[x][y] = arrY[x][y]
            }
        }
    }
}
let a = ans

for(let i = 0; i<n; i++){
    for(let j = 0; j<n-1; j++){
        let tmp = arr[i][j+1]
        arr[i][j+1] = arr[i][j]
        arr[i][j] = tmp // 인접한 x축을 바꾼 후 계산 
        for(let x = 0; x < n; x++){
            for(let y = 0; y<n; y++){
                ans = Math.max(ans,calc(arr,x,y))
            }
        }

        for(let x = 0; x < n; x++){
            for(let y = 0; y<n; y++){
                arr[x][y] = arrY[x][y]
            }
        }
    }
}
console.log(Math.max(a,ans))