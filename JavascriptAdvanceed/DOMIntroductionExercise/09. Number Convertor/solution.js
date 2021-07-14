function solve() {
    let selectMenu = document.getElementById('selectMenuTo')
    let binaryOption = new Option('Binary', 'binary')
    let hexadecimalOption = new Option('Hexadecimal', 'hexadecimal')
    selectMenu.appendChild(binaryOption)
    selectMenu.appendChild(hexadecimalOption)
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
