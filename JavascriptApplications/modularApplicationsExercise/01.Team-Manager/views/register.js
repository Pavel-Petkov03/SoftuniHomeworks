import {html, page} from "../lib.js"
import { endpoints } from "../api.js"
import { validate , generateRequest , retrieveData , setUserInfo , } from "../utils.js"
import { renderModal } from "./modal.js"
const template = () => html`
            <section id="register">
                <article class="narrow">
                    <header class="pad-med">
                        <h1>Register</h1>
                    </header>
                    <form id="register-form" class="main-form pad-large">
                        <div class="error">Error message.</div>
                        <label>E-mail: <input type="text" name="email"></label>
                        <label>Username: <input type="text" name="username"></label>
                        <label>Password: <input type="password" name="password"></label>
                        <label>Repeat: <input type="password" name="repass"></label>
                        <input class="action cta" type="submit" value="Create Account" @click=${register}>
                    </form>
                    <footer class="pad-small">Already have an account? <a href="/login" class="invert">Sign in here</a>
                    </footer>
                </article>
            </section>
`
export function renderRegister(ctx){
    ctx.render(template())
}
async function register(ev){
    ev.preventDefault()
    const {email , password , repass, username} = retrieveData(document.querySelector("form"))
    try {
        validate(email , password , repass)
        const {accessToken, _id} = await generateRequest(endpoints.register, "post", {
            email , password, username
        })
        setUserInfo({
            accessToken , _id
        })
        page.redirect("/")
    }catch (er){
        renderModal(er.message , true)
    }
}









