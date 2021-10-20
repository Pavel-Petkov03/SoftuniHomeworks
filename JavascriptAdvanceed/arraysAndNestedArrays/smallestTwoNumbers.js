function takeTwoSmallest(array){
    return array.sort((a , b) => a-b).slice(0 ,2).join(' ')

}