document.getElementsByTagName("button")[0].addEventListener("click", post)
let form = document.querySelector("form")

async function post(ev) {
    ev.preventDefault()
    let data = new FormData(form)
    let password = data.get("password")
    let email = data.get("email")
    let res = await fetch("http://localhost:3030/users/login", {
        method: 'post',
        headers: {"content-type": "application/json"},
        body: JSON.stringify({
            password, email
        })
    })
    let result = await res.json()
    form.reset()
    if (result.hasOwnProperty("message")){
        alert(result.message)
        return
    }
    sessionStorage.setItem("userData", JSON.stringify({
        email  , id : result._id, accessToken : result.accessToken
    }))
    window.location = "./index.html";
}