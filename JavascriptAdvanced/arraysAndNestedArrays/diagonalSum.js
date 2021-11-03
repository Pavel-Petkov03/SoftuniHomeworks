function diagonalSum(matrix){
    let firstDiagonal = 0
    let secondDiagonal = 0
    for (let first = 0; first < matrix.length; first++){
        firstDiagonal += matrix[first][first]
    }
    let startCol = matrix.length-1
    for (let first = 0; first < matrix.length; first++){
        secondDiagonal += matrix[first][startCol]
        startCol--
    }

    console.log([firstDiagonal, secondDiagonal].join(' '))
}