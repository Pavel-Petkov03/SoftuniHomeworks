import {html} from 'https://unpkg.com/lit-html?module';
import {retrieveData, setUserInfo, validate, generateRequest} from "../utils.js";
import {page} from "../src.js"
const template = () => 
    html`
            <div class="row space-top">
                <div class="col-md-12">
                    <h1>Register New User</h1>
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
                        <div class="form-group">
                            <label class="form-control-label" for="rePass">Repeat</label>
                            <input class="form-control" id="rePass" type="password" name="rePass">
                        </div>
                        <input type="submit" class="btn btn-primary" value="Register" @click="${register}"/>
                    </div>
                </div>
            </form>
    `



async function register(ev){
    ev.preventDefault()
    const {email , password , rePass} = retrieveData(document.querySelector("form"))
    validate(email , password , rePass)
    try {
        const {accessToken, _id} = await generateRequest("http://localhost:3030/users/register", "post", {
            email , password
        })
        setUserInfo({
            accessToken , _id
        })
        page.redirect("/dashboard")
    }catch (er){
        alert(er.message)
    }
}


export  function renderRegister(ctx){
    ctx.render(template())
}