function solve() {
    let selectMenu = document.getElementById('selectMenuTo')
    let binaryOption = document.createElement('option')
    let hexadecimalOption = document.createElement('option')
    binaryOption.appendChild(document.createTextNode('Binary'))
    hexadecimalOption.appendChild(document.createTextNode('Hexadecimal'))
    selectMenu.appendChild(binaryOption)
    selectMenu.appendChild(hexadecimalOption)
    binaryOption.value = 'binary'
    hexadecimalOption.value = 'hexadecimal'
    const myButton = document.getElementsByTagName('button')[0]
    const result = document.getElementById('result')

    function binary(n, r) {
        r.value = n.toString(2)
    }

    function hexadecimal(n, r) {
        r.value =  n.toString(16).toUpperCase()
    }

    myButton.addEventListener('click', () => {
        const num = parseInt(document.getElementById('input').value)
        let myText = selectMenu.value
        switch (myText){
            case 'binary': binary(num, result); break
            case 'hexadecimal' : hexadecimal(num, result); break
        }
    })
}