import { endpoints } from "../api.js"
import {html ,} from "../lib.js"
import { generateRequest } from "../utils.js"


const template = (array) => html`
<section id="catalog-page">
    <h1>All Games</h1>
    ${array.length ? array.map(articleTemplate) : html`<h3 class="no-articles">No articles yet</h3>`}
</section>
`

const articleTemplate = (data) => html`<div class="allGames">
                <div class="allGames-info">
                    <img src=${data.imageUrl}>
                    <h6>Action</h6>
                    <h2>${data.title}</h2>
                    <a href="/details/${data._id}" class="details-button">Details</a>
                </div>
            </div>`



export async function renderCatalog(ctx){
    ctx.render(template(await getData()))
}

async function getData(){
    return await generateRequest(endpoints.allGames , "get")
}
