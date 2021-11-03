function addAndRemove(array) {
    let initial = 1
    let finalArray = []
    for (const element of array) {
        if (element === 'add') {
            finalArray.push(initial)
        } else if (element === 'remove') {
            finalArray.pop()
        }
        initial++
    }
    return finalArray.length > 0 ? finalArray.join('\n') : 'Empty'
}