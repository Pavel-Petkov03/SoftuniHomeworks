function rotateArray(array, number) {
    for (let index = 0; index < number; index++) {
        array.unshift(array.pop())
    }
    return array.join(' ')
}