import {html, page} from "../lib.js"
import { endpoints } from "../api.js"
import { generateRequest , retrieveData , setUserInfo, } from "../utils.js"
const template = () => html`
            <section id="registerPage">
            <form>
                <fieldset>
                    <legend>Register</legend>

                    <label for="email" class="vhide">Email</label>
                    <input id="email" class="email" name="email" type="text" placeholder="Email">

                    <label for="password" class="vhide">Password</label>
                    <input id="password" class="password" name="password" type="password" placeholder="Password">

                    <label for="conf-pass" class="vhide">Confirm Password:</label>
                    <input id="conf-pass" class="conf-pass" name="conf-pass" type="password" placeholder="Confirm Password">

                    <button type="submit" class="register" @click=${register}>Register</button>

                    <p class="field">
                        <span>If you already have profile click <a href="/login">here</a></span>
                    </p>
                </fieldset>
            </form>
        </section>
`
export function renderRegister(ctx){
    ctx.render(template())
}



async function register(ev){
   try{
    ev.preventDefault()
    const {email , password , repass, username} = retrieveData(document.querySelector("form"))
    validate(email , password , repass , email)
    const {accessToken, _id} = await generateRequest(endpoints.register, "post", {
            email , password, username
    })
    setUserInfo({
        accessToken , _id
    })
    page.redirect("/")
   }catch(er){
       alert(er.message)
   }
}


function validate(email , password , repass , username){
    if(email === "" || password === "" || username  == ""){
        throw new Error('all fields must be filled')
    }
    if(password === repass){
        throw new Error('password and repass must match')
    }
}
