
import {html, page} from "../lib.js"
import {retrieveData , generateRequest, getUserInfo,} from "../utils.js"

const template = (data) => html`
    <section id="edit-meme">
            <form id="edit-form">
                <h1>Edit Meme</h1>
                <div class="container">
                    <label for="title">Title</label>
                    <input id="title" type="text" placeholder="Enter Title" name="title" value=${data.title}>
                    <label for="description">Description</label>
                    <textarea id="description" placeholder="Enter Description" name="description">${data.description}</textarea>
                    <label for="imageUrl">Image Url</label>
                    <input id="imageUrl" type="text" placeholder="Enter Meme ImageUrl" name="imageUrl" value=${data.imageUrl}>
                    <input type="submit" class="registerbtn button" value="Edit Meme" @click=${edit.bind(null , data._id)}>
                </div>
            </form>
        </section>
`


async function edit(id , ev){
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    Object.assign(data, {_id : id})
    try{
        await generateRequest(`http://localhost:3030/data/memes/${id}` , "put", data, getUserInfo().accessToken)
        page.redirect(`/details/${id}`)
    }catch(er){
        alert(er.message)
    }
}


export async function renderEditPage(ctx){
    ctx.render(template(await getMeme(ctx.params.id)))
}


async function getMeme(id){
    return await generateRequest(`http://localhost:3030/data/memes/${id}`, "get")
}