function takeTwoArray(array){
    array.sort((a, b) => a-b)
    let center = Number(array.length/2);
    let [firstHalf , secondHalf] = [array.slice(0 , center) , array.slice(center, array.length)];
    if (firstHalf.length === secondHalf.length){
        return secondHalf
    }else{
        return firstHalf.length >= secondHalf.length ? firstHalf : secondHalf
    }
}