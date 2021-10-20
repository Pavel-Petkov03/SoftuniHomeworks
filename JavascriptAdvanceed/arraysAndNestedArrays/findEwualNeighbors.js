function findEqualNeighbors(matrix) {
    function findNeighbors(matrix, row, col) {
        let find = 0
        let symbol = matrix[row][col]
        if (row + 1 >= 0 && row + 1 < matrix.length && matrix[row + 1][col] === symbol) {
            find++
        }
        if (col + 1 >= 0 && col + 1 < matrix[0].length && matrix[row][col + 1] === symbol) {
            find++
        }
        return find
    }

    let all = 0
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            all += findNeighbors(matrix, row, col)
        }
    }
    console.log(all)
}