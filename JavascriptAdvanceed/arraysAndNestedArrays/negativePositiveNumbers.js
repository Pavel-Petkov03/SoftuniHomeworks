function negativePositiveNumbers(array){
    let newArray = []
    for (const element of array) {
        if (element < 0){
            newArray.unshift(element)
        }else{
            newArray.push(element)
        }
    }
   newArray.forEach((x) => console.log(x))
}