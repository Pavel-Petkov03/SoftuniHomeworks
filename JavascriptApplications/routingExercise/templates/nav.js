import {html} from "../src.js"
import { clearUserInfo, getUserInfo } from "../utils.js"
import {page} from "../src.js"

export const nav =  (data) => html`
    <nav>
        <a id="catalogLink" href="/dashboard" class="active">Dashboard</a>
        ${data !== null ? html`
            <div id="user">
                <a id="createLink" href="/create">Create Furniture</a>
                <a id="profileLink" href="/profile/${data._id}">My Publications</a>
                <a id="logoutBtn" href="javascript:void(0)" @click=${logout}>Logout</a>
            </div>
        ` : html`
            <div id="guest">
                <a id="loginLink" href="/login">Login</a>
                <a id="registerLink" href="/register">Register</a>
            </div>
        `}
    </nav>`


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
    page.redirect("/dashboard")
}