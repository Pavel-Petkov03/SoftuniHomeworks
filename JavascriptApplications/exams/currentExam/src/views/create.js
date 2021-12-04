
import { endpoints } from "../api.js"
import {html, page} from "../lib.js"
import { retrieveData, generateRequest, getUserInfo, e } from "../utils.js"
const template = () => html`
            <section class="createPage">
            <form>
                <fieldset>
                    <legend>Add Album</legend>

                    <div class="container">
                        <label for="name" class="vhide">Album name</label>
                        <input id="name" name="name" class="name" type="text" placeholder="Album name">

                        <label for="imgUrl" class="vhide">Image Url</label>
                        <input id="imgUrl" name="imgUrl" class="imgUrl" type="text" placeholder="Image Url">

                        <label for="price" class="vhide">Price</label>
                        <input id="price" name="price" class="price" type="text" placeholder="Price">

                        <label for="releaseDate" class="vhide">Release date</label>
                        <input id="releaseDate" name="releaseDate" class="releaseDate" type="text" placeholder="Release date">

                        <label for="artist" class="vhide">Artist</label>
                        <input id="artist" name="artist" class="artist" type="text" placeholder="Artist">

                        <label for="genre" class="vhide">Genre</label>
                        <input id="genre" name="genre" class="genre" type="text" placeholder="Genre">

                        <label for="description" class="vhide">Description</label>
                        <textarea name="description" class="description" placeholder="Description"></textarea>

                        <button class="add-album" type="submit" @click=${create}>Add New Album</button>
                    </div>
                </fieldset>
            </form>
        </section>
`


export function renderCreate(ctx){
    ctx.render(template())
}


async function create(ev){
    try{
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    validateFields(Object.values(data))
    await generateRequest(endpoints.create, "post", data, getUserInfo().accessToken)
    page.redirect("/catalog")
    }catch(er){
        alert(er.message)
    }
}


function validateFields(data){
    data.forEach(element => {
        if(element === ""){
            throw new Error("All fields must be filled")
        }
    });
}