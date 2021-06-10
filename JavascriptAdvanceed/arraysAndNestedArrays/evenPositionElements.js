function evenPosition(array){
    console.log(array.filter((x,i) => i % 2 === 0).join(' '))
}


function sum(array){
    return Number(array[0]) + Number(array[array.length - 1])
}

function negativePositiveNumbers(array){
    let newArray = []
    for (const element of array) {
        if (element < 0){
            newArray.unshift(element)
        }else{
            newArray.push(element)
        }
    }
   newArray.forEach((x) => console.log(x))

}

function  lastKeyNumbersSequence(times , last){
    let final = [1]
    for(let j = 0; j < times-1; j++){
        if (j < last){
            final.push(final.slice(0, final.length).reduce((a , c) => a+c , 0))
        }else{
            final.push(final.slice(final.length - last, final.length).reduce((a , c) => a+c , 0))
        }
    }
    console.log(final)
}

function takeTwoSmallest(array){
    return array.sort((a , b) => a-b).slice(0 ,2).join(' ')

}

function takeTwoArray(array){
    array.sort((a, b) => a-b)
    let center = Number(array.length/2);
    let [firstHalf , secondHalf] = [array.slice(0 , center) , array.slice(center, array.length)];
    if (firstHalf.length === secondHalf.length){
        console.log(secondHalf)
    }else{
        console.log(firstHalf.length >= secondHalf.length ? firstHalf : secondHalf)
    }
}


function pieceOfPie(array , first , second){
    console.log(array.slice(array.indexOf(first) , array.indexOf(second) + 1))
}


function processOdd(array){
    return array.filter((item , index) => index % 2 !== 0).map(x => 2*x).reverse().join(' ')
}


function getMaxFromMatrix(matrix){
    let max  = matrix[0][0]
    for (let row = 0; row < matrix.length; row++){
        for(let col = 0; col < matrix[row].length; col++){
            if (matrix[row][col] > max){
                max = matrix[row][col]
            }
        }
    }
    console.log(max)
}


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

diagonalSum(
    [[3, 5, 17],
 [-1, 7, 14],
 [1, -8, 89]]

)

function findEqualNeighbors(matrix){
    let all = 0
    for (let row = 0; row < matrix.length; row++){
        for( let col = 0; col < matrix[row].length; col++){
            all += findNeighbors(matrix , row , col)
        }
    }
    console.log(all)
}

function findNeighbors(matrix, row , col){
    let find = 0
    let symbol = matrix[row][col]
    if ( row+1 >= 0 && row +1 < matrix.length && matrix[row+1][col] === symbol){
        find++
    }
    if(col +1 >= 0 && col +1 <  matrix[0].length && matrix[row][col+1] === symbol){
        find++
    }
    return find
}

findEqualNeighbors([['2', '3', '4', '7', '0'],
 ['4', '0', '5', '3', '4'],
 ['2', '3', '5', '4', '2'],
 ['9', '8', '7', '5', '4']]
)




