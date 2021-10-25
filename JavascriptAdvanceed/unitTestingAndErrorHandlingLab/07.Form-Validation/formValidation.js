function validate() {
    const companyInfo = document.getElementById('companyInfo')
    const [username , email , password , confirmPassword , company , companyNumber] = Array.from(document.querySelectorAll("input") )
    const validField = document.getElementById("valid")
    function attachErrorCss(array, command){
        if(command === "error"){
            array.forEach(el => el.style.borderColor = "red")
        }else{
            array.forEach(el => el.style.border = "")
        }
    }


    company.addEventListener("change" , (ev) => {
        if(ev.target.checked){
            companyInfo.style.display = "block"

        }else{
            companyInfo.style.display = "none"
        }
    })

    document.getElementById("submit").addEventListener("click" , (ev) => {
        let valid = true
        ev.preventDefault()
        validField.style.display = "none"
        attachErrorCss([username , email , password , confirmPassword , companyNumber], "")
        if(!(/^[A-Za-z0-9]+$/gm.test(username.value) && username.value.length >= 3 && username.value.length <= 20) ){
            attachErrorCss([username], "error")
            valid = false
        }
        if(!(/^\w+$/gm.test(password.value) && password.value.length >= 5 && password.value.length <= 15)){
            attachErrorCss([password], "error")
            valid = false
        }
        if(!(/^\w+$/gm.test(confirmPassword.value) && confirmPassword.value.length >= 5 && confirmPassword.value.length <= 15)){
            attachErrorCss([confirmPassword], "error")
            valid = false
        }
        if(password.value !== confirmPassword.value){
            attachErrorCss([password , confirmPassword], "error")
            valid = false
        }
        if(!/[a-zA-Z0-9]+@[a-zA-Z0-9]+\..+/gm.test(email.value)){
            attachErrorCss([email], "error")
            valid= false
        }
        if(companyInfo.style.display === "block" && Number(companyNumber.value) < 1000 || Number(companyNumber.value) > 9999){
            attachErrorCss([companyNumber], "error")
            valid= false
        }
        if(valid){
            validField.style.display = "block"
        }
    })
}