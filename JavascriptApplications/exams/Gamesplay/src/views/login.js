import {html, page} from "../lib.js"
import { generateRequest, retrieveData , setUserInfo} from "../utils.js"
import {endpoints } from "../api.js"
const template = () => html`
<section id="login-page" class="auth">
<section id="login">
    <form id="login">
    <div class="container">
        <div class="brand-logo"></div>
        <h1>Login</h1>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" placeholder="Sokka@gmail.com">

        <label for="login-pass">Password:</label>
        <input type="password" id="login-password" name="password">
        <input type="submit" class="btn submit" value="Login" @click=${login}>
        <p class="field">
            <span>If you don't have profile click <a href="#">here</a></span>
        </p>
    </div>
    </form>
</section>

`



export function renderLogin(ctx){
    ctx.render(template())
}

async function login(ev){
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    const {_id , accessToken} = await generateRequest(endpoints.login, "post", data)
    setUserInfo({
            accessToken , _id
    })
    page.redirect("/")
}






