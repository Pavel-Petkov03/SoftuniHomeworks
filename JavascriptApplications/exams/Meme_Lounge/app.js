import {render, page} from "./lib.js"

import { renderDetailsPage } from "./views/details.js"
import { renderCreate } from "./views/create.js"
import { renderHome } from "./views/home.js"
import { renderEditPage } from "./views/edit.js"
import {renderLogin} from "./views/login.js"
import { renderMyProfile } from "./views/my-profile.js"
import { renderRegister } from "./views/register.js"
import {navTemplate } from "./views/nav.js"
import {getUserInfo} from "./utils.js"
import { renderAllMemes } from "./views/allMemes.js"

const root = document.querySelector("#container")

page(decorateRender)
page("/login", renderLogin)
page("/register", renderRegister)
page("/", renderHome)
page("/create", renderCreate)
page("/details/:id", renderDetailsPage)
page("/edit/:id" , renderEditPage)
page("/profile/:id", renderMyProfile)
page("/all-memes" , renderAllMemes)
page("/my-profile" , renderMyProfile)


page.start()





function decorateRender(ctx , next){
    ctx.render = (content) => render(content, root)
    ctx.redirect = (url) => page.redirect(url)
    render(navTemplate(getUserInfo()) , document.querySelector("nav"))
    next()
}