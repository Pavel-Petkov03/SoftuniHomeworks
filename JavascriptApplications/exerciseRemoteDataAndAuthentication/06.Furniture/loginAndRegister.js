import {generateRequest, retrieveData} from "../utils.js"


window.addEventListener("load" , () => {
    const eventListeners = [registerUser , loginUser]
    const buttons = [...document.querySelectorAll("button")]
    buttons.forEach((el , index) => el.addEventListener("click", eventListeners[index]))
})

const [registerForm , loginForm] = document.querySelectorAll("form")
async function loginUser(ev){
    ev.preventDefault()
    let data = retrieveData(loginForm)
    try {
        let response = await generateRequest("http://localhost:3030/users/login" ,"post" , data)
        saveInStorage(response.accessToken)
    }catch (er){
        alert("Some error has occurred")
    }
}

async function registerUser(ev){
    console.log()
    ev.preventDefault()
    let {email , password , rePass} = retrieveData(registerForm)
    try {
        validateUser( password , rePass, email)
        try{
            let data = await generateRequest("http://localhost:3030/users/register" , "post" , {
                email , password
            } )
            saveInStorage(data.accessToken)
        }catch (er){
            alert("server error has occurred")
        }
    }
    catch (er){
        alert(er.message)
    }
}


function validateUser(password , confirmPassword , email){
    let errorMessage = ""
    if(password !== confirmPassword){
        errorMessage = "the password and repeat password must match"
    }else if(password.length <= 10 || password.length >= 20){
        errorMessage = "the password must be between 10 and 20 symbols"
    }else if(!validateEmail(email)){
        errorMessage = "the email should be valid"
    }
    if (errorMessage){
        throw new Error(errorMessage)
    }
}






function saveInStorage(accessToken){
    sessionStorage.clear()
    sessionStorage.setItem("userData" , accessToken)
    location.href = "home.html"
}

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}