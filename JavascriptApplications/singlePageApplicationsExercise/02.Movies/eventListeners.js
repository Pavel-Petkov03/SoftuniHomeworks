import {generateRequest, retrieveData, validate } from "../utils.js";
import {homeRouter, detailsRouter} from "./routers.js";
const container = document.getElementById("container")
let userData

async function addMovie(){
    userData = JSON.parse(sessionStorage.getItem(`userData`))
    const data = retrieveData(document.querySelector("form"))
    Object.assign(data,  {_ownerId : userData._id})
    try {
        console.log(userData)
        await generateRequest("http://localhost:3030/data/movies/", "post", data, userData.accessToken)
        container.innerHTML = ""
        await homeRouter()
    }catch (er){
        alert(er.message)
    }
}

async function register(ev){
    ev.preventDefault()
    const {repeatPassword , password, email} = retrieveData(document.querySelector("form"))

    try {
        validate(email , password, repeatPassword)
        const {_id, accessToken} = await generateRequest("http://localhost:3030/users/register/", "post", {
            password , email
        })
        sessionStorage.setItem("userData", JSON.stringify({
            email, _id, accessToken
        }))
        container.innerHTML = ""
        await homeRouter()
        document.location.reload()
    }catch (er){
        alert(er.message)
    }
}

async function login(ev){
    ev.preventDefault()
    const {password, email} = retrieveData(document.querySelector("form"))
    try {
        const {_id, accessToken} = await generateRequest("http://localhost:3030/users/login/", "post", {
            password , email
        })
        sessionStorage.setItem("userData", JSON.stringify({
            email , _id, accessToken
        }))
        container.innerHTML = ""
        await homeRouter()
        document.location.reload()
    }catch (er){
        alert(er.message)
    }
}
async function edit(ev){
    ev.preventDefault()
    userData = JSON.parse(sessionStorage.getItem(`userData`))
    const id = ev.target.dataset.id
    const data = retrieveData(document.querySelector("form"))
    try {
        await generateRequest("http://localhost:3030/data/movies/" + id, "put", data, userData.accessToken)
        await detailsRouter(ev)

    }catch (er){
        alert(er.message)
    }
}

async function unlike(ev){
    ev.preventDefault()
    userData = JSON.parse(sessionStorage.getItem(`userData`))
    const movieId = ev.target.parentNode.querySelector("h3").dataset.id
    // this is like id
    try {
        const data = await generateRequest(`http://localhost:3030/data/likes?where=movie_id%3D%22${movieId}%22%20and%20_ownerId%3D%22${userData._id}%22`)
        await generateRequest("http://localhost:3030/data/likes/" + data[0]._id, "delete", null, userData.accessToken)
        ev.target.textContent = "Like"
        ev.target.removeEventListener("click", unlike)
        ev.target.addEventListener("click", like)
        ev.target.className = "btn btn-primary"
    }catch (er){
        alert(er.message)
    }
}

async function like(ev){
    userData = JSON.parse(sessionStorage.getItem(`userData`))
    ev.preventDefault()
    const id = ev.target.parentNode.querySelector("h3").dataset.id
    try {
       const [_ , length] = await Promise.all([
            generateRequest(`http://localhost:3030/data/likes`, "post", {
                movie_id : id}, userData.accessToken),
            generateRequest(`http://localhost:3030/data/likes?where=movie_id%3D%22${id}%22&distinct=_ownerId&count`, "get")
        ])
        ev.target.removeEventListener("click", like)
        ev.target.addEventListener("click", unlike)
        ev.target.textContent = `Liked ${length}`
        ev.target.className = "btn btn-success"
    }catch (er){
        alert(er.message)
    }
}

async function onDelete(ev){
    userData = JSON.parse(sessionStorage.getItem(`userData`))
    ev.preventDefault()
    const id = ev.target.parentNode.querySelector("h3").dataset.id
    container.innerHTML = ""
    try {
        await generateRequest("http://localhost:3030/data/movies/"+id, "delete", null, userData.accessToken)
        await homeRouter()
    }catch (er){
        alert(er.message)
    }
}

export {
    addMovie,
    register,
    login,
    edit,
    like ,
    onDelete,
    unlike
}