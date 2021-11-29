import { html } from "../lib.js"
import { generateRequest , getUserInfo} from "../utils.js"

const template = (currentUserId , data) => html`
    <section id="meme-details">
            <h1>Meme Title: ${data.title}</h1>
            <div class="meme-details">
                <div class="meme-img">
                    <img alt="meme-alt" src="${data.imageUrl}">
                </div>
                <div class="meme-description">
                    <h2>Meme Description</h2>
                    <p>
                        ${data.description}
                    </p>

                    <!-- Buttons Edit/Delete should be displayed only for creator of this meme  -->
                    ${currentUserId === data._ownerId ? html`
                    <a class="button warning" href="/edit/${data._id}">Edit</a>
                    <button class="button danger" @click=${onDelete.bind(null , data._id)}>Delete</button>` 
                    : null}
                </div>
            </div>
        </section>
`


async function loadDetails(id){
    return await generateRequest(`http://localhost:3030/data/memes/${id}`, "get")
}

async function onDelete(id , ev){
    ev.preventDefault()
    try{
        await generateRequest(`http://localhost:3030/data/memes/${id}`, "delete", null , getUserInfo().accessToken)
    }catch(er){
        alert(er.message)
    }
}

export async function renderDetailsPage(ctx){
    let _id 
    if(getUserInfo()){
        _id = getUserInfo()._id
    }
    const memeId = ctx.params.id
    const data = await loadDetails(memeId)
    ctx.render(template(_id , data))
}
