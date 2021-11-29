import {getUserInfo, clearUserInfo } from "../utils.js"
import { html , page} from "../lib.js"

const navTemplate = (isAutenticated) => html`
            <a href="/all-memes">All Memes</a>
             <!-- Logged users -->
             ${isAutenticated ? html`<div class="user">
                <a href="/create">Create Meme</a>
                <div class="profile">
                    <span>Welcome, ${isAutenticated.email}</span>
                    <a href="/my-profile">My Profile</a>
                    <a href="/logout" @click=${logout}>Logout</a>
                </div>
            </div>` : html`
            <div class="guest">
                <div class="profile">
                    <a href="/login">Login</a>
                    <a href="/register">Register</a>
                </div>
                <a class="active" href="/">Home Page</a>
            </div>`}
            
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
    page.redirect("/")
}

export {
    navTemplate
}