function aggregateElements(array){
    console.log(array.reduce((a , b) => a+b, 0))
    console.log(array.reduce((a , b) => a + 1 /b  , 0))
    console.log(array.join(''))

}


aggregateElements([1,2,3])
