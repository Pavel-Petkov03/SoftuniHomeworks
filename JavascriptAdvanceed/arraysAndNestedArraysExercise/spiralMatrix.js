function spiralMatrix(r , c) {
    const results = [];
    for (let i = 0; i < r; i++) {
        results.push([]);
    }
    let counter = 1;
    let startColumn = 0;
    let endColumn = c - 1;
    let startRow = 0;
    let endRow = r - 1;
    let printMatrix = (m) => {
        m.forEach(array => console.log(array.join(' ')))
    }
    while (startColumn <= endColumn && startRow <= endRow) {
        for (let i = startColumn; i <= endColumn; i++) {
            results[startRow][i] = counter;
            counter++;
        }
        startRow++;
        for (let i = startRow; i <= endRow; i++) {
            results[i][endColumn] = counter;
            counter++;
        }
        endColumn--;
        for (let i = endColumn; i >= startColumn; i--) {
            results[endRow][i] = counter;
            counter++;
        }
        endRow--;
        for (let i = endRow; i >= startRow; i--) {
            results[i][startColumn] = counter;
            counter++;
        }
        startColumn++;
    }
    printMatrix(results)
}