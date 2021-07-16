function solve() {
    let words = document.getElementById('text').value.split(' ');
    words.forEach((el, index, array) => {
        array[index] = el.toLowerCase()
    });

    function capitalizeMassive(start , words){
        for (let index = start; index < words.length; index++){
                let newWord = words[index].split('')
                newWord[0] = newWord[0].toUpperCase()
                words[index] = newWord.join('')
            }
        return words
    }
    const letterCase = document.getElementById("naming-convention").value;
    switch (letterCase) {
        case 'Camel Case':
            words = capitalizeMassive(1 , words)
            break
        case 'Pascal Case' :
            words = capitalizeMassive(0 , words)
            break
        default:
            words = ['Error!']
    }
    let result = document.getElementById('result')
    result.textContent = words.join('')
}