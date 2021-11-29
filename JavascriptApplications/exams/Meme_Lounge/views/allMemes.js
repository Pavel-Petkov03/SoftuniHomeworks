import {html} from "../lib.js"
import { generateRequest } from "../utils.js"

const allMemesTemplate = (array) =>  html`
    <section id="meme-feed">
                <h1>All Memes</h1>
                <div id="memes">
                    ${array.length > 0 ? array.map(memeTemplate) :  html`<p class="no-memes">No memes in database.</p>`}
                </div>
            </section>
`
const memeTemplate = (data) => html`
    <div class="meme">
                        <div class="card">
                            <div class="info">
                                <p class="meme-title">${data.title}</p>
                                <img class="meme-image" alt="meme-img" src="${data.imageUrl}">
                            </div>
                            <div id="data-buttons">
                                <a class="button" href="/details/${data._id}">Details</a>
                            </div>
                        </div>
    </div>`


async function getAllMembers(){
    return await generateRequest("http://localhost:3030/data/memes?sortBy=_createdOn%20desc", "get")
}

export async function renderAllMemes(ctx){
    ctx.render(allMemesTemplate(await getAllMembers()))
}