function diagonalAttack(matrix) {
    matrix = matrix.map(array => array.split(' ').map(el => parseInt(el)))
    let firstDiagonalSum = 0
    let col = 0
    let secondDiagonal = 0
    let unwantedCord = []
    let makeChange = (m, changeValue, cord) => {
        for (let row = 0; row < m.length; row++) {
            for (let col = 0; col < m.length; col++) {
                if (!cord.some(ar => ar[0] === row && ar[1] === col)) {
                    m[row][col] = changeValue
                }
            }
        }
        return m
    }
    let printMatrix = (m) => {
        m.forEach(array => console.log(array.join(' ')))
    }

    for (let s = 0; s < matrix.length; s++) {
        firstDiagonalSum += matrix[s][s]
        unwantedCord.push([s, s])
    }
    for (let row = matrix.length - 1; row >= 0; row--) {
        secondDiagonal += matrix[row][col]
        unwantedCord.push([row, col])
        col++
    }
    if (firstDiagonalSum === secondDiagonal) {
        matrix = makeChange(matrix, firstDiagonalSum, unwantedCord)
    }
    printMatrix(matrix)
}
