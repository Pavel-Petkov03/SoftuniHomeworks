


function magicMatrix(matrix) {
    let newMassive = []
    let helper = []
    let len = matrix[0].length
    for (let row = 0; row < len; row++) {
        for (let col = 0; col < matrix.length; col++) {
            helper.push(matrix[col][row])
        }
        newMassive.push(helper)
        helper = []
    }
    newMassive.push(...matrix)
    let wantedValues = matrix[0].reduce((summer, a) => summer + a, 0)
    return newMassive.every(array => array.reduce((summer, a) => summer + a, 0) === wantedValues)
}