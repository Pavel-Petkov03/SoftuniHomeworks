import {html, render, page} from "../lib.js"
import { getUserInfo , clearUserInfo} from "../utils.js"
const template = (data) => html`
            <h1><a class="home" href="/">GamesPlay</a></h1>
            <nav>
            <a href="/catalog">All games</a>
                ${data ? html`<div id="user">
                    <a href="/create">Create Game</a>
                    <a href="/logout" @click=${logout}>Logout</a>
                </div>` : html`
                <div id="guest">
                    <a href="/login">Login</a>
                    <a href="/register">Register</a>
                </div>`}
            </nav>
`





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


export function renderNav(){
    render(template(getUserInfo()), document.querySelector("header"))
}