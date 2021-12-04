import {page, render} from "./lib.js"
import {renderNav} from "./views/navbar.js"
import { renderBrowse } from "./views/browse.js"
import { renderCreate } from "./views/create.js"
import { renderLogin } from "./views/login.js"
import { renderRegister } from "./views/register.js"
import { renderMyProfile } from "./views/myTeam.js"
import { renderHome } from "./views/home.js"
import { renderEdit } from "./views/edit.js"
import { renderDetails } from "./views/details.js"


const root = document.querySelector("main")

page(loadMiddleware)
page("/browse", renderBrowse)
page("/create", renderCreate)
page("/login", renderLogin)
page("/register", renderRegister)
page("/my-profile/:id", renderMyProfile)
page("/", renderHome)
page("/edit/:id", renderEdit)
page("/details/:id" , renderDetails)
page("/edit/:id", renderEdit)

page.start()


function loadMiddleware(ctx , next){
    ctx.render = (template) => render(template , root)
    renderNav()
    next()
}



