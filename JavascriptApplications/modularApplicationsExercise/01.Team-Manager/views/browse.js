 import {html, until, page} from "../lib.js"
 import { generateRequest } from "../utils.js"
 import {endpoints} from "../api.js"
 import { articleTemplate } from "./teamView.js"
const browseTemplate = (isAuthenticated, data) => html`
    <div id="browse">

        <article class="pad-med">
            <h1>Team Browser</h1>
        </article>
        ${isAuthenticated ? html`<article class="layout narrow">
            <div class="pad-small"><a href="/create" class="action cta">Create Team</a></div>
        </article>` : until(data, html`<p>Loading...</p>`)}
    </div>
 `



async function browseData() {
    const data =  await generateRequest(endpoints.teams, "get")
    return data.map(articleTemplate)
}

export async function renderBrowse(ctx){
    ctx.render(browseTemplate(false, await browseData()))
}
