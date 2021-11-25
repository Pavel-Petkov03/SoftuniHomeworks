import {render} from "./src.js"
import {page} from "./src.js"
import { renderCatalog } from "./templates/catalog.js"
import { renderCreate } from "./templates/create.js"
import { renderDelete } from "./templates/delete.js"
import { renderDetailsPage } from "./templates/details.js"
import { renderEditPage } from "./templates/edit.js"
import {renderLogin} from "./templates/login.js"
import { renderProfile } from "./templates/myProfile.js"
import { renderRegister } from "./templates/register.js"
import {nav } from "./templates/nav.js"
import {getUserInfo} from "./utils.js"

const root = document.querySelector(".container")

page(decorateRender)
page("/login", renderLogin)
page("/register", renderRegister)
page("/dashboard", renderCatalog)
page("/create", renderCreate)
page("/details/:id", renderDetailsPage)
page("/edit/:id" , renderEditPage)
page("/delete/:id", renderDelete)
page("/profile/:id", renderProfile)
page.start()





function decorateRender(ctx , next){
    ctx.render = (content) => render(content, root)
    ctx.redirect = (url) => page.redirect(url)
    render(nav(getUserInfo()), document.querySelector("header"))
    next()
}