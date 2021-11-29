import {html , page} from "../lib.js"
import {retrieveData , setUserInfo , generateRequest} from "../utils.js"

const loginTemplate = () => html`
    <section id="login">
            <form id="login-form">
                <div class="container">
                    <h1>Login</h1>
                    <label for="email">Email</label>
                    <input id="email" placeholder="Enter Email" name="email" type="text">
                    <label for="password">Password</label>
                    <input id="password" type="password" placeholder="Enter Password" name="password">
                    <input type="submit" class="registerbtn button" value="Login" @click=${login}>
                    <div class="container signin">
                        <p>Dont have an account?<a href="/register">Sign up</a>.</p>
                    </div>
                </div>
            </form>
        </section>
`

function renderLogin(ctx){
    ctx.render(loginTemplate())
}
export {
    renderLogin
}

async function login(ev){
    ev.preventDefault()
    const {email , password} = retrieveData(document.querySelector("form"))
    console.log(email , password);
    try {
        if(email === "" || password === ""){
            throw new Error("All fields must be filled")
        }
        const {_id , accessToken , gender , username} = await generateRequest("http://localhost:3030/users/login", "post", {
            email , password
        })
        setUserInfo({
            accessToken , _id, email, gender , username
        })
        page.redirect("/all-memes")
    }catch (er){
        alert(er.message)
    }
}