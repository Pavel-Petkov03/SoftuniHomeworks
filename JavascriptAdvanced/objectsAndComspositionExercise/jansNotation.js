jansNotation = (array) => {
    let operands = ['/', '*', '+', '-']
    let numArray = []
    for (const argument of array) {
        if (operands.includes(argument)) {
            if (numArray.length >= 2) {
                let [second, first] = [numArray.pop(), numArray.pop()]
                numArray.push(eval(`${first}
                ${argument}
                ${second} `))
            } else {
                return `Error: not enough operands!`
            }
        } else {
            numArray.push(argument)
        }
    }
    if (numArray.length === 1) {
        return numArray[0]
    } else {
        return `Error: too many operands!`
    }
}