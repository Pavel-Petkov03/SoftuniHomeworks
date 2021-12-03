
import {html, page } from "../lib.js"
import {retrieveData , generateRequest, getUserInfo, errorBox} from "../utils.js"

const template = () => html`
    <section id="create-meme">
            <form id="create-form">
                <div class="container">
                    <h1>Create Meme</h1>
                    <label for="title">Title</label>
                    <input id="title" type="text" placeholder="Enter Title" name="title">
                    <label for="description">Description</label>
                    <textarea id="description" placeholder="Enter Description" name="description"></textarea>
                    <label for="imageUrl">Meme Image</label>
                    <input id="imageUrl" type="text" placeholder="Enter meme ImageUrl" name="imageUrl">
                    <input type="submit" class="registerbtn button" value="Create Meme" @click=${create}>
                </div>
            </form>
        </section>
`
async function create(ev){
    ev.preventDefault()
    try{
        const data = retrieveData(document.querySelector("form"))
        validate(data)
        await generateRequest("http://localhost:3030/data/memes", "post", data, getUserInfo().accessToken)
        page.redirect("/all-memes")
    }catch(er){
        errorBox(er.message)
    }
}

function validate(entries){
    for (const [key ,val] of Object.entries(entries)) {
        if((val) === ""){
            throw new Error(`${key} must be filled`)
        }
    }
}


export function renderCreate(ctx){
    ctx.render(template())
}