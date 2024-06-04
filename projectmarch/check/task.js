function findOdd(a) {
    console.log(typeof a)
    a.sort((x, y) => x - y)
    // console.log(a.filter((arbuz) => arbuz!=0))
    // for (var i = 0; i < a.lenght; i++) {
        // console.log(a)
        // let result = a[i-1]
        // if (a[i] == a[i-1]) {
        //     result = result ^ a[i]
        // }  
        // else {
        //     if (result != 0) 
        //     return a[i]

        //     result = a[i]
        // }
    // }
    // console.log(a.lenght)
    // console.log()
    // if (a.lenght % 2 == 0) {
    //     return 0
    //   }
    // else {
    let result = 0
    let last = 0
    for (arbuz of a){
        // console.log(last)
        if (last != arbuz & result != 0) {
            return last
        }
        last = arbuz
        result = result^arbuz
    }
    return result}
//   }

let x = [1, 0, 0, 1, 0]
console.log(findOdd(x))
console.log(x.length)