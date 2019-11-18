# JS 함수 사용법

```javascript
//forEach

let v = [1,2,3,4,5];

v.forEach(item => {
	console.log(item)
})
// 1 2 3 4 5

//some
v.some(item => {
    if(v == 2)
        console.log(v)
    return v==2;
})
// return 값이 트루이면 종료.
```

