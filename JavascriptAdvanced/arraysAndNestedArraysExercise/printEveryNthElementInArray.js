function nthNumber(array, number) {
    let newArray = []
    for (let index = 0; index <= array.length; index += number) {
        newArray.push(array[index])
    }
    return newArray
}