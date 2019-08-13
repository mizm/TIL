
// 반복 1- while
let i = 0;
while (i<10){
    console.log(i);
    i++;
}

// 반복 2- for
for (let j=0;j<10;j++)
{
    console.log(j);
}

// 반복 3 - for of
for (let number of [1,2,3,4,5])// const로도 선언가능
{
    console.log(number);
}

// 배열
const numbers = [1,2,3,4]
console.log(numbers[-1])//안됨
numbers.length
console.log(numbers.reverse())//원본변경
console.log(numbers)
numbers.push('a')//반환값 length
numbers.pop()
numbers.unshift('a')//앞쪽에 넣기
numbers.includes(1)//포함여부
numbers.indexOf('a')//인덱스 반환 왼쪽부터 처음찾아지는인덱스 없는 인자 -1 반환
console.log(numbers.join('/'))//default = ','
numbers.slice(0,2)// numbers[0:2]
numbers.filter(function(x){return x>1}) // [1,2,3,4]

const me = {
    name : 'miz',
    'phoneNumber' : '12341234',
    appleProducts: {
        ipad : false,
        iphone : 'O'
    }
}
// me['name']
// me.name

// // JSON - JavaScript Object Notation (JS 객체 표기법)
// JSON.stringify() // Object To String

// JSON.parse() // JSON String To Object

// 함수
// 방법 1
function add(num1,num2){
    return num1 + num2
}
console.log('add:'+add(1,2))

// 방법 2
const sub = function (num1,num2) {
    return num1 - num2
}
console.log('sub : ' + sub(5,3))

typeof add // function
typeof sub // function

// Arrow Function
// const mul = function(num1,num2) {
//     return num1*num2
// }
const mul = (num1,num2) => {
    return num1 * num2
}

let square = (num) => { return num ** 2}

// return 문 단 한 줄이면 {} return 생략가능
square = (num) => num ** 2


// ()안의 인자가 단 하나일경우 () 생략가능
sqaure = num => num**2
// 0개 일 때는 생략 불가능
let noAgrs = () => 'No args'
// object return 시 () 생략 불가
let returnObject = () => ({key:'value'})

// 함수의 기본 인자
const sayHello = (name = 'noName') => `hi${name}`

console.log(sayHello(),sayHello('john'))

// noname function 익명함수
// function(num) {return num ** 3}
// (num) => {return num ** 0.5}
// 익명 함수 즉시 호출
console.log( (function(num){return num ** 3})(3) )
const concat = (str1,str2) => {
    return `${str1} - ${str2}`
}
const checkLongStr = (string) => {
    if(string.length > 10)
    {
        return true
    }
    else 
    {
        return false
    }
}

if(checkLongStr(concat('Happy','Hacking')))
{
    console.log('LONG STRING')
}
else
{
    console.log('SHORT STRING')
}