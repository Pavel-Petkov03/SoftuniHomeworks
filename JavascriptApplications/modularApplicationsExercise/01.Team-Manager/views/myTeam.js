import {html, until} from "../lib.js"
import { generateRequest} from "../utils.js"
import {endpoints} from "../api.js"
import {articleTemplate} from "./teamView.js"
const myProfileTemplate = (data) => html`
    <section id="my-teams">

        <article class="pad-med">
            <h1>My Teams</h1>
        </article>
        ${until(data, html`<p>Loading...</p>`)}
        <article class="layout narrow">
            <div class="pad-med">
                ${data.length === 0 ? html`<p>You are not a member of any team yet.</p>
                <p><a href="/browse">Browse all teams</a> to join one, or use the button bellow to cerate your own
                    team.</p>` : null}
            </div>
            <div class=""><a href="/create" class="action cta">Create Team</a></div>
        </article>
    </section>
`

async function loadMyTeams(id){
    const  data = await generateRequest(endpoints.teamsForParticularMember(id), "get")
    return data.map(articleTemplate)
}


export function renderMyProfile(ctx){
    console.log(ctx.params.id);
    ctx.render(myProfileTemplate(loadMyTeams(ctx.params.id)))
}