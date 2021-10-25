function reg(sentence){
    let exp = /[A-Za-z0-9]+/gi;
    return (sentence.match(exp)).join(', ').toUpperCase()
}