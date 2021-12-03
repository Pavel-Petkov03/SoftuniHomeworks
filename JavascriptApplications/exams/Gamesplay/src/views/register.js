import {html, page} from "../lib.js"
import { endpoints } from "../api.js"
import {generateRequest , retrieveData , setUserInfo , } from "../utils.js"
const template = () => html`
<section id="register-page" class="content auth">
<form id="register">
                <div class="container">
                    <div class="brand-logo"></div>
                    <h1>Register</h1>

                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" placeholder="maria@email.com">

                    <label for="pass">Password:</label>
                    <input type="password" name="password" id="register-password">

                    <label for="con-pass">Confirm Password:</label>
                    <input type="password" name="confirm-password" id="confirm-password">

                    <input class="btn submit" type="submit" value="Register" @click=${register}>

                    <p class="field">
                        <span>If you already have profile click <a href="/login">here</a></span>
                    </p>
                </div>
            </form>

</section>
             
`

async function register(ev){
    ev.preventDefault()
    const input = retrieveData(document.querySelector("form"))
    const {email , password , username} = input
    const repass = input["confirm-password"]
    try{
        validate(email , password , repass , username)
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
    if(email === "" || password == "" || username === ""){
        throw new Error("all fields must be filled")
    }
    console.log(password, repass);
    if(password !== repass){
        throw new Error("password and confirm password must match")
    }
}
 
export function renderRegister(ctx){
    ctx.render(template())
}