import {html, page} from "../lib.js"
import { generateRequest, retrieveData , setUserInfo} from "../utils.js"
import {endpoints } from "../api.js"
const template = () => html`
<section id="loginPage">
            <form>
                <fieldset>
                    <legend>Login</legend>

                    <label for="email" class="vhide">Email</label>
                    <input id="email" class="email" name="email" type="text" placeholder="Email">

                    <label for="password" class="vhide">Password</label>
                    <input id="password" class="password" name="password" type="password" placeholder="Password">

                    <button type="submit" class="login" @click=${login}>Login</button>

                    <p class="field">
                        <span>If you don't have profile click <a href="/register">here</a></span>
                    </p>
                </fieldset>
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