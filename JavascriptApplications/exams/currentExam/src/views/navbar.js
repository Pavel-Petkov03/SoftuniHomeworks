import {html, render,  page} from "../lib.js"
import { getUserInfo , clearUserInfo} from "../utils.js"
const template = (data) => html`
            <nav>
            <img src="./images/headphones.png">
            <a href="/">Home</a>
            <ul>
                <!--All user-->
                <li><a href="/catalog">Catalog</a></li>
                <li><a href="/search">Search</a></li>
                ${data ?  html`
                <li><a href="/create">Create Album</a></li>
                <li><a href="" @click=${logout}>Logout</a></li>` : html`
                <!--Only user-->
                <li><a href="/login">Login</a></li>
                <li><a href="/register">Register</a></li>`
            }
            </ul>
        </nav>
`





export function renderNav(){
    render(template(getUserInfo()), document.querySelector("header"))
}


async function logout(ev){
    ev.preventDefault()
    await fetch("http://localhost:3030/users/logout" , {
        headers : {
            "content-type" : "application/json",
            "x-authorization" : getUserInfo().accessToken
        },
        method : "get"
    })
    clearUserInfo()
    page.redirect("/login")
}