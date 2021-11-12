

document.querySelector("button").addEventListener("click" , post)
async function post(ev){
    ev.preventDefault()
    let form = document.querySelector("form")
    let data = new FormData(form)
    let email = data.get("email")
    let password = data.get("password")
    let repass = data.get("rePass")
    form.reset()
    if(password !== repass){
        alert("Password and confirm password are different")
        return
    }
    let res = await fetch("http://localhost:3030/users/register" , {
        method : "post",
        headers : {"content-type" : "application/json"},
        body : JSON.stringify({
            email , password
        })
    })
    let result = await res.json()
    if(result.message){
        alert(result.message)
        return
    }

    sessionStorage.setItem("userData", JSON.stringify({
        email  , id : result._id, accessToken : result.accessToken
    }))
    window.location = "./index.html";
}