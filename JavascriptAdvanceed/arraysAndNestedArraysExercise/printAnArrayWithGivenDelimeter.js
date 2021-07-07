function join(array, delimiter) {
    return array.join(delimiter)
}


function nthNumber(array, number) {
    let newArray = []
    for (let index = 0; index <= array.length; index += number) {
        newArray.push(array[index])
    }
    return newArray
}

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


function rotateArray(array, number) {
    for (let index = 0; index < number; index++) {
        array.unshift(array.pop())
    }
    return array.join(' ')
}

function createDecreasingSubsequence(array) {
    let newArray = []
    let biggest = array[0]
    for (const element of array) {
        if (element >= biggest) {
            newArray.push(element)
            biggest = element
        }
    }
    return newArray
}

function ListOfNames(array) {
    return array.sort((a, b) => a.localeCompare(b)).map((el, index) => {
        return `${index + 1}.${el}`
    }).join('\n')
}


function sortingNumbers(array) {
    let newArray = []
    let len = array.length
    array.sort((a, b) => a - b)
    for (let it = 0; it < len / 2; it++) {
        newArray.push(array.shift())
        newArray.push(array.pop())
    }
    return newArray.filter(el => el !== undefined)
}


function sortByTwoCriteria(array) {
    array.sort((current , next) => {
        if(current.length === next.length){
            return current.localeCompare(next)
        }
        return current.length - next.length
    })
    array.forEach(el => console.log(el))
}


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


function ticTacToe(matrix) {
    let checkForValidity = (array) => {
        return array.every(val => val !== false) && array.every(val => val === array[0])
    }
    let changePlayer = (player) => {
        if (player === 'X') {
            return 'O'
        }
        return 'X'
    }
    let printResult = (m) => {
        console.log(`${m[0][0]}\t${m[0][1]}\t${m[0][2]}`)
        console.log(`${m[1][0]}\t${m[1][1]}\t${m[1][2]}`)
        console.log(`${m[2][0]}\t${m[2][1]}\t${m[2][2]}`)
    }
    let checkForWin = (matrix) => {
        let horizontal = []
        let vertical = []
        let firstDiagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
        let secondDiagonal = [matrix[2][0], matrix[1][1], matrix[0][2]]
        for (let row = 0; row <= 2; row++) {
            for (let col = 0; col <= 2; col++) {
                horizontal.push(matrix[row][col])
                vertical.push(matrix[col][row])
            }
            if (checkForValidity(horizontal) || checkForValidity(vertical)) {
                return true
            }
            horizontal = []
            vertical = []
        }
        return checkForValidity(firstDiagonal) || checkForValidity(secondDiagonal)
    }
    let initialMatrix = [[false, false, false],
        [false, false, false],
        [false, false, false]]
    let isWinner = false
    let takenPlaces = 0
    let startTupleOfCord = 0
    let row
    let col
    let startPlayer = 'O'
    while (!isWinner && takenPlaces !== 9) {
        [row, col] = [...matrix[startTupleOfCord].split(' ').map(x => Number(x))]
        startTupleOfCord++
        if (initialMatrix[row][col] === false) {
            startPlayer = changePlayer(startPlayer)
            initialMatrix[row][col] = startPlayer
            takenPlaces++
            isWinner = checkForWin(initialMatrix)
        } else {
            console.log(`This place is already taken. Please choose another!`)
        }
    }


    if (isWinner) {
        console.log(`Player ${startPlayer} wins!`)
    } else {
        console.log(`The game ended! Nobody wins :(`)
    }
    printResult(initialMatrix)
}

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


function orbit(array) {
    [width, height, rowPos, colPos] = [...array.map(el => parseInt(el))]
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