import {html, page} from "../lib.js"
import { generateRequest, retrieveData , setUserInfo} from "../utils.js"
import {endpoints } from "../api.js"
import { renderModal}   from "./modal.js"
const template = () => html`
<section id="login">
                <article class="narrow">
                    <header class="pad-med">
                        <h1>Login</h1>
                    </header>
                    <form id="login-form" class="main-form pad-large">
                        <div class="error">Error message.</div>
                        <label>E-mail: <input type="text" name="email"></label>
                        <label>Password: <input type="password" name="password"></label>
                        <input class="action cta" type="submit" value="Sign In" @click=${login}>
                    </form>
                    <footer class="pad-small">Don't have an account? <a href="/register" class="invert">Sign up here</a>
                    </footer>
                </article>
            </section>
`
export function renderLogin(ctx){
    ctx.render(template())
}

async function login(ev){
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    try {
        const {_id , accessToken} = await generateRequest(endpoints.login, "post", data)
        setUserInfo({
            accessToken , _id
        })
        page.redirect("/")
    }catch (er){
        renderModal(er.message , true)
    }
}

