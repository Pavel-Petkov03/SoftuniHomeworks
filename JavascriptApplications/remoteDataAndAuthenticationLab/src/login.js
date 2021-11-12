import {generateRequest, retrieveData} from "../utils.js";
document.getElementById("login").addEventListener(`click` , login)
async function login(ev){
    ev.preventDefault()
    let {password , email} = retrieveData(document.querySelector("form"))
    try {
        let {accessToken , _id} = await generateRequest("http://localhost:3030/users/login", "post", {
            password , email
        })
        sessionStorage.setItem("userData", JSON.stringify({
            accessToken, _id
        }))
        document.location.href = "create.html"
    }catch (er){
        alert(er.message)
    }
}