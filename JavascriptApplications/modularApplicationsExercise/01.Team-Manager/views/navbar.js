import {html, render, page} from "../lib.js"
import { getUserInfo , clearUserInfo} from "../utils.js"
const template = (data) => html`
            <nav>
            <a href="/browse" class="action">Browse Teams</a>
                ${data ?  html`<a href="/my-profile/${data._id}" class="action">My Teams</a><a href="#" class="action" @click=${logout}>Logout</a>` 
                : html`<a href="/login" class="action">Login</a><a href="/register" class="action">Register</a>`}
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