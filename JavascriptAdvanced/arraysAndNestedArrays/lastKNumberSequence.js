function  lastKeyNumbersSequence(times , last){
    let final = [1]
    for(let j = 0; j < times-1; j++){
        if (j < last){
            final.push(final.slice(0, final.length).reduce((a , c) => a+c , 0))
        }else{
            final.push(final.slice(final.length - last, final.length).reduce((a , c) => a+c , 0))
        }
    }
    return final
}
lastKeyNumbersSequence(6,
3)