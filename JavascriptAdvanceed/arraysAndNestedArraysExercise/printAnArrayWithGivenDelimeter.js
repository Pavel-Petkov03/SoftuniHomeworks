

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

function  ListOfNames(array){
    array.sort((a , b) => a-b)
    let newArray = []
    for (let index=0; index < array.length; index++){
        newArray.push(`${index+1}.${array[index]}`)
    }
    return newArray.join('\n')
}


console.log(ListOfNames(
    ["John", "Bob", "Christina", "Ema"]
))



function sortingNumbers(array) {
    let helper = array.clone()
    array.sort(function (a,b){
        if(a === Math.max(helper) ){

        }
    })
}


function sortByTwoCriteria(array){
    array.sort(function (a , b){

    })
}

function Equals(matrix){

}