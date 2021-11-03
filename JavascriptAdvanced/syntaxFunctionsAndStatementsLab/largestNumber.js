function chooseLargest(a , b,  c){
    let temp = NaN
    if (a > b && a > c){
        temp = a
    }
    else if (b > c && b > a){
        temp = b
    }
    else{
        temp = c
    }
    console.log(`The largest number is ${temp}.`)
}



chooseLargest(5, -3, 16)