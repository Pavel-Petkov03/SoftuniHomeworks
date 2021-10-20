function processOdd(array){
    return array.filter((item , index) => index % 2 !== 0).map(x => 2*x).reverse().join(' ')
}