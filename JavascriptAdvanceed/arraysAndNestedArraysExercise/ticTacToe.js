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
