import {html} from "../src.js"
import { generateRequest, getUserInfo } from "../utils.js"
import { furnitureTemplate } from "./furnitureTemplate.js"


const catalogTemplate = (array) => html `
    <div class="row space-top">
                <div class="col-md-12">
                    <h1>Welcome to Furniture System</h1>
                    <p>Select furniture from the catalog to view details.</p>
                </div>
            </div>
            <div class="row space-top">
                ${array.map(el => furnitureTemplate(el , getUserInfo()))}
            </div>
`




async function loadAll(){
    return await generateRequest("http://localhost:3030/data/catalog", "get")
}

export async function renderCatalog(ctx){
    ctx.render(catalogTemplate(await loadAll()))
}