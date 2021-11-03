function validate() {
    const email = document.getElementById("email")
    email.addEventListener("change", (ev) => {
        ev.preventDefault()
        const emailText = email.value
        if(validateEmail(emailText)){
            email.classList.remove("error")
        }else{
            email.classList.add("error")
        }
    })

    function validateEmail(email){
        const regex = /[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z0-9]+/
        return regex.test(email)
    }
}