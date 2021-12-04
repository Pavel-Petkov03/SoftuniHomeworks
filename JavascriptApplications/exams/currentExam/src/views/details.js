import { endpoints } from "../api.js"
import { html } from "../lib.js"
import { generateRequest, getUserInfo } from "../utils.js"



const template = (data, currentId) => html`
<section id="detailsPage">
            <div class="wrapper">
                <div class="albumCover">
                    <img src=${data.imgUrl}>
                </div>
                <div class="albumInfo">
                    <div class="albumText">

                        <h1>Name: ${data.name}</h1>
                        <h3>Artist: ${data.artist}</h3>
                        <h4>Genre: ${data.genre}</h4>
                        <h4>Price: ${data.price}</h4>
                        <h4>Date: ${data.releaseDate}</h4>
                        <p>Description: ${data.description}</p>
                    </div>
                    ${console.log(data._ownerId , currentId)}
                    ${data._ownerId === currentId ? html`<div class="actionBtn">
                        <a href="/edit/${data._id}" class="edit">Edit</a>
                        <a href="#" class="remove" @click=${onDelete.bind(null , data._id)}>Delete</a>
                    </div>` : null}
                </div>
            </div>
        </section>
`



async function onDelete(id , ev){
    ev.preventDefault()
    await generateRequest(endpoints.delete(id) , "delete" , null , getUserInfo().accessToken)
    page.redirect("/")
}

export async function renderDetails(ctx){
    let currentId = getUserInfo()
    console.log(currentId)
    if(currentId){
        currentId = currentId._id
    }
    ctx.render(template(await getData(ctx.params.id), currentId))
}

async function getData(id){
    return await generateRequest(endpoints.details(id))
}