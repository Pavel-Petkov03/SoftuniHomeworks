function pieceOfPie(array , first , second){
    return  array.slice(array.indexOf(first) , array.indexOf(second) + 1)
}