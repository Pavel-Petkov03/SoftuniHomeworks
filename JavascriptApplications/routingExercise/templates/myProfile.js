import {html , } from "../src.js"
import { generateRequest , getUserInfo} from "../utils.js"
import { furnitureTemplate } from "./furnitureTemplate.js"

const myProfileTemplate  = (array) => html`
    <div class="row space-top">
                <div class="col-md-12">
                    <h1>My Furniture</h1>
                    <p>This is a list of your publications.</p>
                </div>
            </div>
            <div class="row space-top">
            ${array.map(el => furnitureTemplate(el , getUserInfo()))}
            </div>
    `
export async function renderProfile(ctx){
    const id  = ctx.params.id
    const data = await generateRequest(`http://localhost:3030/data/catalog?where=_ownerId%3D%22${id}%22`, "get")
    ctx.render(myProfileTemplate(data))
}