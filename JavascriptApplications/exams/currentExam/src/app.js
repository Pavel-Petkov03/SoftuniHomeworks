import {render, page} from "./lib.js"
import { renderCatalog } from "./views/catalog.js"
import { renderCreate } from "./views/create.js"
import { renderDetails } from "./views/details.js"
import { renderEdit } from "./views/editPage.js"
import { renderHomePage } from "./views/homePage.js"
import { renderLogin } from "./views/login.js"
import { renderNav } from "./views/navbar.js"
import { renderRegister } from "./views/register.js"
import { renderSearch } from "./views/search.js"
const root = document.querySelector("#box")
page(decorator)
page("/", renderHomePage)
page("/details/:id", renderDetails)
page("/edit/:id", renderEdit)
page("/login", renderLogin)
page("/register", renderRegister)
page("/catalog", renderCatalog)
page("/create", renderCreate)
page("/search" , renderSearch)
page.start()


function decorator(ctx, next){
    renderNav()
    ctx.render = (template) =>  render(template, root )
    next()
}
