import {generateRequest, retrieveData, validateUser} from "../utils.js"
document.getElementById("register").addEventListener("click", register)
async function register(ev){
    ev.preventDefault()
    let body = retrieveData(document.querySelector("form"))
    try {
        let {password , rePass, email, accessToken, _id} = await generateRequest("http://localhost:3030/users/register", "post", body)
        validateUser(password , rePass, email)
        sessionStorage.setItem("userData", JSON.stringify({
            accessToken, _id
        }))
        document.location.href = "create.html"
    }catch (er){
        alert(er.message)
    }
}