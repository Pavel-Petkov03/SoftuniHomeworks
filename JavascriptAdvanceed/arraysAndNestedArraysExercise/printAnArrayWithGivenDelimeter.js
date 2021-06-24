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
    array.sort((a, b) => a - b)
    let newArray = []
    for (let index = 0; index < array.length; index++) {
        newArray.push(`${index + 1}.${array[index]}`)
    }
    return newArray.join('\n')
}


function sortingNumbers(array) {
    let helper = array.clone()
    array.sort(function (a, b) {
        if (a === Math.max(helper)) {

        }
    })
}


function sortByTwoCriteria(array) {
    array.sort(function (a, b) {

    })
}

function magicMatrix(matrix) {
    let newMassive = []
    let helper = []
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            helper.push(matrix[col][row])
        }
        newMassive.push(helper)
        helper = []
    }
    newMassive.push(...matrix)
    let wantedValues = matrix[0].reduce((summer, a) => summer + a, 0)
    return newMassive.every(array => array.reduce((summer, a) => summer + a, 0) === wantedValues)
}

console.log(
    magicMatrix(
        [[1, 0, 0],
            [0, 0, 1],
            [0, 1, 0]]
    )
)


function ticTacToe(matrix) {
    let initialMatrix = [[false, false, false],
        [false, false, false],
        [false, false, false]]
    let row
    let col
    let index = 0
    for (const cord of matrix) {
        row = cord[0]
        col = cord[1]
        if(matrix[row][col] !== false){
            console.log()
        }else{
            let checkForWin = (row , col) => {

            }
        }
    }
}