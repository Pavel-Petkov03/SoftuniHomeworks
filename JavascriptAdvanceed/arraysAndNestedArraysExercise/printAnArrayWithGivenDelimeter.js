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
    array.sort(function (a, b) {
        return a - b
    })
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
    let initialMatrix = [[false, false, false],
        [false, false, false],
        [false, false, false]]
    let isWinner = false
    let takenPlaces = 0
    let startTupleOfCord = 0
    let row
    let col
    let startPlayer = 'O'
    let changePlayer = (player) => {
        if (player === 'X') {
            return 'O'
        }
        return 'X'
    }
    while (!isWinner && takenPlaces !== 9) {
        [row, col] = [...matrix[startTupleOfCord].split(' ').map(x => Number(x))]
        startTupleOfCord++
        if (initialMatrix[row][col] === false) {
            startPlayer = changePlayer(startPlayer)
            initialMatrix[row][col] = startPlayer
            takenPlaces++
            isWinner = checkForWin(initialMatrix)
        }else{
            console.log(`This place is already taken. Please choose another!`)
        }
    }

    let printResult  = () => {
        console.log(`${initialMatrix[0][0]}\t${initialMatrix[0][1]}\t${initialMatrix[0][2]}`)
        console.log(`${initialMatrix[1][0]}\t${initialMatrix[1][1]}\t${initialMatrix[1][2]}`)
        console.log(`${initialMatrix[2][0]}\t${initialMatrix[2][1]}\t${initialMatrix[2][2]}`)
    }
    if(isWinner){
        console.log(`Player ${startPlayer} wins!`)
    }else{
        console.log(`The game ended! Nobody wins :(`)
    }
    printResult()
}


function checkForWin(matrix) {
    if (matrix[0][0] === matrix[0][1] === matrix[0][2] !== false) {
        return true
    } else if (matrix[1][0] === matrix[1][1] === matrix[1][2] !== false) {
        return true
    } else if (matrix[2][0] === matrix[2][1] === matrix[2][2] !== false) {
        return true
    } else if (matrix[0][0] === matrix[1][1] === matrix[2][2] !== false) {
        return true
    } else if (matrix[2][0] === matrix[1][1] === matrix[0][2] !== false) {
        return true
    } else if (matrix[0][0] === matrix[0][1] === matrix[0][2] !== false) {
        return true
    } else if (matrix[1][0] === matrix[1][1] === matrix[1][2] !== false) {
        return true
    } else if (matrix[2][0] === matrix[2][1] === matrix[2][2] !== false) {
        return true
    }
    return false
}


ticTacToe(
        ["0 1",
             "0 0",
             "0 2",
             "2 0",
             "1 0",
             "1 1",
             "1 2",
             "2 2",
             "2 1",
             "0 0"]
)

