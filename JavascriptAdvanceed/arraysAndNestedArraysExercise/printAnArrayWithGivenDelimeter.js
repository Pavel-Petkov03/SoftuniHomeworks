

function join(array, delimiter){
    return array.join(delimiter)
}


function nthNumber(array , number){
    let newArray = []
    for(let index=0; index <= array.length; index += number){
        newArray.push(array[index])
    }
    return newArray
}

function addAndRemove(array){
    let initial = 1
    let finalArray = []
    for (const element of array) {
        if(element === 'add'){
            finalArray.push(initial)
        }else if (element === 'remove'){
            finalArray.pop()
        }
        initial++
    }
        return finalArray.length > 0 ? finalArray.join('\n') : 'Empty'
}



function  rotateArray(array , number){
    for(let index = 0; index < number; index++){
        array.unshift(array.pop())
    }
    return array.join(' ')
}

console.log(
rotateArray(
    ['1',
'2',
'3',
'4'],
2

))

function  createDecreasingSubsequence(array){
    let newArray = []
    let biggest = array[0]
    for (const element of array) {
        if(element >= biggest){
            newArray.push(element)
            biggest = element
        }
    }
    return newArray
}

console.log(createDecreasingSubsequence(
    [1,
3,
8,
4,
10,
12,
3,
2,
24]

))

function  ListOfNames(array){
    array = array.sort()
    for (let index=0; index < array.length; index++){
        console.log(`${index+1}.${array[index]}`)
    }
}


ListOfNames(
        ["John", "Bob", "Christina", "Ema"]
)