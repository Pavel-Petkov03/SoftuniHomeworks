import { endpoints } from "../api.js"
import {html, page} from "../lib.js"
import { generateRequest , getUserInfo} from "../utils.js"
import { getAllComments , commentTemplate, postComment} from "./comments.js"


const template = (data, currentId, comments) => html`
<h1>Game Details</h1>
            <div class="info-section">

                <div class="game-header">
                    <img class="game-img" src=${data.imageUrl} />
                    <h1>${data.title}</h1>
                    <span class="levels">MaxLevel: ${data.maxLevel}</span>
                    <p class="type">${data.category}</p>
                </div>

                <p class="text">${data.summary}</p>
                <div class="details-comments">
                    ${comments.length ? html`<h2>Comments:</h2><ul>${comments.map(commentTemplate)}</ul>` : html`<p class="no-comment">No comments.</p>`  }
                </div>
                ${data._ownerId === currentId ? html`
                <div class="buttons">
                    <a href="/edit/${data._id}" class="button">Edit</a>
                    <a href="#" class="button" @click=${onDelete.bind(null , data._id)}>Delete</a>
                </div>
                ` : null}
            </div>
            ${ currentId !== null && data._ownerId !== currentId ? html`
            <article class="create-comment">
                <label>Add new comment:</label>
                <form class="form">
                    <textarea name="comment" placeholder="Comment......"></textarea>
                    <input class="btn submit" type="submit" value="Add Comment" @click=${postComment.bind(null, data._id)}>
                </form>
            </article>
            ` : null}
`


async function retrieveDetailsData(id){
    return await generateRequest(endpoints.details(id))
}

async function onDelete(id , ev){
    ev.preventDefault()
    await generateRequest(endpoints.delete(id) , "delete" , null , getUserInfo().accessToken)
    page.redirect("/")
}


export async function renderDetails(ctx){
    let info = getUserInfo()
    if(info){
        info = info._id
    }
    const comments = await getAllComments(ctx.params.id)
    const data = await retrieveDetailsData(ctx.params.id)
    ctx.render(template(data, info, comments))
}
