calorieObject = (array) => {
    let obj = {}
    for (let index = 0; index < array.length; index += 2) {
        obj[array[index]] = parseInt(array[index + 1])
    }
    return obj
}