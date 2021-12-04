import { endpoints } from "../api.js"
import {html, render} from "../lib.js"
import { generateRequest } from "../utils.js"
import { articleTemplate } from "./articleTemplate.js"

const template = () => html`
<section id="searchPage">
            <h1>Search by Name</h1>

            <div class="search">
                <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
                <button class="button-list" @click=${search}>Search</button>
            </div>

            <h2>Results:</h2>

            <!--Show after click Search button-->
            <div class="search-result">
            </div>
        </section>
`

async function search(ev){
    ev.preventDefault()
    const value = document.querySelector("#search-input").value
    const data = await getData(value)
    render(resultTemplate(data), document.querySelector(".search-result"))
}

const resultTemplate = (data) => html`
    ${data.length ? data.map(articleTemplate) : html`<p class="no-result">No result.</p>`}
`



async function getData(data){
    return await generateRequest(endpoints.search(data))
}


export function renderSearch(ctx){
    ctx.render(template())
}