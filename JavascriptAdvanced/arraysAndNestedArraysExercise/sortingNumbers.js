function sortingNumbers(array) {
    let newArray = []
    let len = array.length
    array.sort((a, b) => a - b)
    for (let it = 0; it < len / 2; it++) {
        newArray.push(array.shift())
        newArray.push(array.pop())
    }
    return newArray.filter(el => el !== undefined)
}