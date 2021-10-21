function orbit(array) {
    let [width, height, rowPos, colPos] = [array.map(el => parseInt(el))]
    let matrix = []
    let printMatrix = (m) => {
        m.forEach(array => console.log(array.join(' ')))
    }
    for (let row = 0; row < height; row++) {
        matrix.push([])
        for (let col = 0; col < width; col++) {
            if (rowPos !== row || colPos !== col) {
                matrix[row][col] = Math.max(Math.abs(rowPos - row), Math.abs(colPos - col)) + 1
            }

        }

    }
    matrix[rowPos][colPos] = 1
    printMatrix(matrix)
}