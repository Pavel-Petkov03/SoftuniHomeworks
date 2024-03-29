import {generateRequest, retrieveData, validateUser} from "../utils.js"


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
        saveInStorage(response)
    }catch (er){
        alert("Some error has occurred")
    }
}

async function registerUser(ev){
    ev.preventDefault()
    let {email , password , rePass} = retrieveData(registerForm)
    try {
        validateUser( password , rePass, email)
        try{
            let data = await generateRequest("http://localhost:3030/users/register" , "post" , {
                email , password
            } )
            saveInStorage(data)
        }catch (er){
            alert("server error has occurred")
        }
    }
    catch (er){
        alert(er.message)
    }
}
function saveInStorage(data){
    sessionStorage.clear()
    sessionStorage.setItem("userData" , JSON.stringify({
        id : data._id , accessToken : data.accessToken
    }))
    location.href = "home.html"
}