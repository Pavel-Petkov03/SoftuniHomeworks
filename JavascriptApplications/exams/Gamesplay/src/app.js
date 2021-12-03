import {page , render}  from "./lib.js"
import { renderCatalog } from "./views/catalog.js"
import { renderCreate } from "./views/create.js"
import { renderDetails } from "./views/details.js"
import { renderEdit } from "./views/edit.js"
import { renderLogin } from "./views/login.js"
import { renderNav } from "./views/navbar.js"
import {renderRegister} from "./views/register.js"
import { renderWelcomePage } from "./views/welcomePage.js"

const root = document.querySelector("#box")


page(decorator)
page("/edit/:id" , renderEdit)
page("/login" , renderLogin)
page("/register" , renderRegister)
page("/create" , renderCreate)
page("/details/:id" , renderDetails)
page("/catalog" , renderCatalog)
page("/" , renderWelcomePage)
page.start()




function decorator(ctx , next){
    ctx.render = (template ) => render(template , root)
    renderNav()
    next()
}



