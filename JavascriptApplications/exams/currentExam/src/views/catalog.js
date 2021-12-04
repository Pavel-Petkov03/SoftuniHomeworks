import { endpoints } from "../api.js"
import {html} from "../lib.js"
import { generateRequest } from "../utils.js"
import { articleTemplate } from "./articleTemplate.js"

const template = (array) => html`
    
    <section id="catalogPage">
        <h1>All Albums</h1>
        ${array.length ? array.map(articleTemplate) : html`<p>No Albums in Catalog!</p>`}
    </section>
    
`




async function getData(){
    return await generateRequest(endpoints.catalog, "get")
}

export async function renderCatalog(ctx){
    ctx.render(template(await getData()))
}