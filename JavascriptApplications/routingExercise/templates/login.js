import {html} from "../src.js"
import {retrieveData, setUserInfo, generateRequest} from "../utils.js";
import {page} from "../src.js"
const template = () =>
    html`
        <div class="container">
            <div class="row space-top">
                <div class="col-md-12">
                    <h1>Login User</h1>
                    <p>Please fill all fields.</p>
                </div>
            </div>
            <form>
                <div class="row space-top">
                    <div class="col-md-4">
                        <div class="form-group">
                            <label class="form-control-label" for="email">Email</label>
                            <input class="form-control" id="email" type="text" name="email">
                        </div>
                        <div class="form-group">
                            <label class="form-control-label" for="password">Password</label>
                            <input class="form-control" id="password" type="password" name="password">
                        </div>
                        <input type="submit" class="btn btn-primary" value="Login" @click="${login}"/>
                    </div>
                </div>
            </form>
        </div>
    `
async function login(ev){
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    try {
        const {_id , accessToken} = await generateRequest("http://localhost:3030/users/login", "post", data)
        setUserInfo({
            accessToken , _id
        })
        page.redirect("/dashboard")
    }catch (er){
        alert(er.message)
    }
}

export function renderLogin(ctx){
    ctx.render(template())
}