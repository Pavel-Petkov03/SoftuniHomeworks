import {e} from "../../utils.js"
import {registerRouter, loginRouter} from "../routers.js"

const logout = e("a", {className : "nav-link", href : void(0), textContent : `Logout`})
const register  =  e("a", {className : "nav-link", href : void(0), textContent : `Register`})
const login  =  e("a", {className : "nav-link", href : void(0), textContent : `Login`})
register.addEventListener("click", registerRouter)
login.addEventListener("click", loginRouter)
const ar = [null , registerRouter, loginRouter]
const textArray = [null , "Register", "Login"]
logout.addEventListener("click", async (ev) => {
    ev.preventDefault()
    sessionStorage.clear()
    loginRouter(ev)
    Array.from(document.querySelectorAll("nav a")).forEach((el , index) => {
        if (index > 0){
            el.addEventListener("click", ar[index])
            el.textContent = textArray[index]
        }
    })
})
function authenticateNavbar(){
    const user = JSON.parse(sessionStorage.getItem("userData"))
    let arrayOfLi
    if (user){
        arrayOfLi = [
            e("li" , {className : "nav-item"}, [
                e("a", {className : "nav-link", href : void(0), textContent : `Welcome ${user.email}`})
            ]),
            e("li" , {className : "nav-item"}, [
                logout
            ]),
        ]
    }else{
        arrayOfLi = [
            e("li" , {className : "nav-item"}, [
                login
            ]),
            e("li" , {className : "nav-item"}, [
                register
            ]),
        ]
    }
    return arrayOfLi
}

export async function navbarComponent(){
    return e("nav", {className : "navbar navbar-expand-lg navbar-dark bg-dark "}, [
        e("a", {className : "navbar-brand text-light", href : void(0), textContent : 'Movies'}),
        e("ul", {className : "navbar-nav ml-auto"} , [
            ...authenticateNavbar()
        ])
    ])
}
