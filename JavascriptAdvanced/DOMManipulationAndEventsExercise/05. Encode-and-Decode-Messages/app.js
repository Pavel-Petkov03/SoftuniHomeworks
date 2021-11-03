function encodeAndDecodeMessages() {
    let [firstTextArea , secondTextArea] = document.querySelectorAll('textarea')
    let [firstButton, secondButton] = document.querySelectorAll('button')
    firstButton.addEventListener('click' , () => {
        secondTextArea.value = firstTextArea.value.split('').map(el => String.fromCharCode(el.charCodeAt(0) + 1)).join('')
        firstTextArea.value = ''
    })
    secondButton.addEventListener('click', ()=> {
        secondTextArea.value = secondTextArea.value.split('').map(el => String.fromCharCode(el.charCodeAt(0) - 1)).join('')
    })
}