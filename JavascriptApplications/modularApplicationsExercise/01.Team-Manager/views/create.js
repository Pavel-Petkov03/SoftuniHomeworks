
import { endpoints } from "../api.js"
import {html, page} from "../lib.js"
import { retrieveData, generateRequest, getUserInfo } from "../utils.js"
import { handleModal } from "./modal.js"

const template = () => html`
            <section id="create">
                <article class="narrow">
                    <header class="pad-med">
                        <h1>New Team</h1>
                    </header>
                    <form id="create-form" class="main-form pad-large">
                        <label>Team name: <input type="text" name="name"></label>
                        <label>Logo URL: <input type="text" name="logoUrl"></label>
                        <label>Description: <textarea name="description"></textarea></label>
                        <input class="action cta" type="submit" value="Create Team" @click=${create}>
                    </form>
                </article>
            </section>
`
export function renderCreate(ctx){
    ctx.render(template())
}


async function create(ev){
    ev.preventDefault()
    handleModal("Do you realy want to create team" , true , true , async () => {
        const data = retrieveData(document.querySelector("form"))
        validateFields(data)
        await generateRequest(endpoints.teams, "post", data, getUserInfo().accessToken)
        page.redirect("/my-profile")
    })
}


const validateObj = {
    name : (value) => value.length > 4,
    logoUrl : (value) => value.length > 0,
    description : (value) => value.length > 10,
}

function validateFields(object){
    for (const [key , val] of Object.entries(object)) {
        if(!validateObj[key](val)){
            throw new Error(`${key} must be filled correctly`)
        }
    }
}