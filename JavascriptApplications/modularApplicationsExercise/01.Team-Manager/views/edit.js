import { endpoints } from "../api.js"
import {html, page} from "../lib.js"
import { handleModal } from "./modal.js"
import { generateRequest, retrieveData , getUserInfo } from "../utils.js"

const template = (id) => html`
    <section id="edit">
        <article class="narrow">
            <header class="pad-med">
                <h1>Edit Team</h1>
            </header>
            <form id="edit-form" class="main-form pad-large">
                <label>Team name: <input type="text" name="name"></label>
                <label>Logo URL: <input type="text" name="logoUrl"></label>
                <label>Description: <textarea name="description"></textarea></label>
                <input class="action cta" type="submit" value="Save Changes" @click=${edit.bind(null , id)}>
            </form>
        </article>
    </section>
`
export function renderEdit(ctx){
    ctx.render(template(ctx.params.id))
}

async function edit(id , ev){
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    Object.assign(data, {_id : id})
    handleModal("Do you want to edit this team" , true , true , async () => {
        await generateRequest(endpoints.currentTeam(id) , "put", data, getUserInfo().accessToken)
        page.redirect(`/details/${id}`)
    })
}





