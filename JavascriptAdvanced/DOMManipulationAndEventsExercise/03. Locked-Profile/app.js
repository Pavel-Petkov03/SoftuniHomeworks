function lockedProfile() {
    let allUsers = Array.from(document.querySelectorAll('.profile'))
    allUsers.forEach(el => {
        const userInformation = el.querySelector('div')
        const showButton = el.querySelector('button')
        showButton.addEventListener('click' ,(ev) => {
            const checkboxButtonInfo = getTextContent(Array.from(el.querySelectorAll('input')).slice(0,2))
            if(checkboxButtonInfo === 'unlock' && showButton.textContent === 'Show more'){
                userInformation.removeAttribute('id')
                showButton.textContent = 'Hide it'
            }
            else if(checkboxButtonInfo === 'unlock' && showButton.textContent === 'Hide it'){
                userInformation.setAttribute('id', `user${allUsers.indexOf(el)+1}HiddenFields`)
                showButton.textContent = 'Show more'
            }
        })
    })


    function getTextContent(array){
        for (const check of array) {
            if(check.checked){
                return check.value
            }
        }
    }
}