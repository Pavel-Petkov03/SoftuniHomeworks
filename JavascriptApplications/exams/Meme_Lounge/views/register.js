import {html , page} from "../lib.js"
import {retrieveData , setUserInfo , generateRequest} from "../utils.js"

const registerTemplate = () => html`
    <section id="register">
            <form id="register-form">
                <div class="container">
                    <h1>Register</h1>
                    <label for="username">Username</label>
                    <input id="username" type="text" placeholder="Enter Username" name="username">
                    <label for="email">Email</label>
                    <input id="email" type="text" placeholder="Enter Email" name="email">
                    <label for="password">Password</label>
                    <input id="password" type="password" placeholder="Enter Password" name="password">
                    <label for="repeatPass">Repeat Password</label>
                    <input id="repeatPass" type="password" placeholder="Repeat Password" name="repeatPass">
                    <div class="gender">
                        <input type="radio" name="gender" id="female" value="female">
                        <label for="female">Female</label>
                        <input type="radio" name="gender" id="male" value="male" checked>
                        <label for="male">Male</label>
                    </div>
                    <input type="submit" class="registerbtn button" value="Register" @click=${register}>
                    <div class="container signin">
                        <p>Already have an account?<a href="/login">Sign in</a>.</p>
                    </div>
                </div>
            </form>
        </section>
`

function renderRegister(ctx){
    ctx.render(registerTemplate())
}
export {
    renderRegister
}

async function register(ev){
    ev.preventDefault()
    const {email , password , repeatPass, gender, username} = retrieveData(document.querySelector("form"))
    try {
        validate({email , password , repeatPass , username})
        const {accessToken, _id} = await generateRequest("http://localhost:3030/users/register", "post", {
            email , password, gender , username
        })
        setUserInfo({
            accessToken , _id,  username , email, gender
        })
        page.redirect("/all-memes")
    }catch (er){
        alert(er.message)
    }
}


function validate(obj){
    console.log(obj);
    Object.values(obj).forEach(el => {
        if(el === ""){
            throw new Error("All fields must be filled")
        }
    })
    if(obj.password !== obj.repeatPass){
        throw new Error("password and confirm password must match")
    }
}
// todo error 
