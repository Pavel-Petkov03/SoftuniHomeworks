import { endpoints } from "../api.js"
import {html, page} from "../lib.js"
import { generateRequest, retrieveData , getUserInfo } from "../utils.js"

const template = (data) => html`
    <section class="editPage">
            <form>
                <fieldset>
                    <legend>Edit Album</legend>

                    <div class="container">
                        <label for="name" class="vhide">Album name</label>
                        <input id="name" name="name" class="name" type="text" value=${data.name}>

                        <label for="imgUrl" class="vhide">Image Url</label>
                        <input id="imgUrl" name="imgUrl" class="imgUrl" type="text" value=${data.imgUrl}>

                        <label for="price" class="vhide">Price</label>
                        <input id="price" name="price" class="price" type="text" value=${data.price}>

                        <label for="releaseDate" class="vhide">Release date</label>
                        <input id="releaseDate" name="releaseDate" class="releaseDate" type="text" value=${data.releaseDate}>

                        <label for="artist" class="vhide">Artist</label>
                        <input id="artist" name="artist" class="artist" type="text" value=${data.artist}>

                        <label for="genre" class="vhide">Genre</label>
                        <input id="genre" name="genre" class="genre" type="text" value=${data.genre}>

                        <label for="description" class="vhide">Description</label>
                        <textarea name="description" class="description" rows="10"cols="10">${data.description}</textarea>
                        <button class="edit-album" type="submit" @click=${edit.bind(null , data._id)}>Edit Album</button>
                    </div>
                </fieldset>
            </form>
        </section>
`

export async function renderEdit(ctx){
    const data = await getPageData(ctx.params.id)
    ctx.render(template(data))
}

async function edit(id , ev){
    try{
        ev.preventDefault()
        const data = retrieveData(document.querySelector("form"))
        validate(Object.values(data))
        await generateRequest(endpoints.details(id) , "put", data, getUserInfo().accessToken)
        page.redirect(`/details/${id}`)
    }catch(er){
        alert(er.message)
    }
}



async function getPageData(id){
    return await generateRequest(endpoints.details(id), "get")
}

function validate(array){
    array.forEach(element => {
        if(element === ""){
            throw new Error("All fields must be filled")
        }
    });
}