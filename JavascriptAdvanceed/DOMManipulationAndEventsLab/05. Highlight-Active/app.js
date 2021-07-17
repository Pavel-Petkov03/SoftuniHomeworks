function focused() {
    Array.from(document.querySelectorAll('input')).forEach(el => {
        el.addEventListener('focus', (event) => event.target.parentNode.classList.add('focused'))
        el.addEventListener('blur', (event) =>  event.target.parentNode.classList.remove('focused'))

    })

}