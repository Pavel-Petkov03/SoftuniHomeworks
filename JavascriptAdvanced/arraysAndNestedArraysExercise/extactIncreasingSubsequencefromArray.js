function createDecreasingSubsequence(array) {
    let newArray = []
    let biggest = array[0]
    for (const element of array) {
        if (element >= biggest) {
            newArray.push(element)
            biggest = element
        }
    }
    return newArray
}