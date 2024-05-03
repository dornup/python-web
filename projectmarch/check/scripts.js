// function test() {
//     console.log(123);
// }
// dom - document object model
// let btn = document.querySelector('button');
// // btn.addEventListener('click', test)
// btn.addEventListener('click', () => {
//     console.log(11);
// })

// btn.addEventListener('click', () => {
//     console.log(111);
// })

// btn.addEventListener('mouseover', () => {
//     console.log(122);
// })

// btn.addEventListener('mouseout', () => {
//     console.log(333);
// })
/* function a() {
     return 42
}
a.pupupu = 62
a.a = a

console.log(a.a)

let dict = {} // object
let list = [] // array */

let array = [2, -2, 0, -1, 1, '2', '-1', '1', '-2', '0']
console.log(array.sort()) // каког...

let btn = document.querySelector('button');
btn.addEventListener('mouseover', () => {
     btn.classList.add('classno');
});

btn.addEventListener('click', () => {
     btn.classList.remove('classno');
});