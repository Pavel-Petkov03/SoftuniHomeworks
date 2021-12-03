import { endpoints } from "../api.js"
import {html, page} from "../lib.js"
import { generateRequest, retrieveData , getUserInfo } from "../utils.js"

const template = (data, id) => html`
<section id="edit-page" class="auth">
<form id="edit">
                <div class="container">

                    <h1>Edit Game</h1>
                    <label for="leg-title">Legendary title:</label>
                    <input type="text" id="title" name="title" value=${data.title}>

                    <label for="category">Category:</label>
                    <input type="text" id="category" name="category" value=${data.category}>

                    <label for="levels">MaxLevel:</label>
                    <input type="number" id="maxLevel" name="maxLevel" min="1" value=${data.maxLevel}>

                    <label for="game-img">Image:</label>
                    <input type="text" id="imageUrl" name="imageUrl" value=${data.imageUrl}>

                    <label for="summary">Summary:</label>
                    <textarea name="summary" id="summary">${data.summary}</textarea>
                    <input class="btn submit" type="submit" value="Edit Game" @click=${edit.bind(null , id)}>

                </div>
            </form>
        </section>
    
`


export async function renderEdit(ctx){
    const data = await retrieveDetailsData(ctx.params.id) 
    ctx.render(template(data, ctx.params.id))
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

async function retrieveDetailsData(id){
    return await generateRequest(endpoints.details(id))
}



function validate(ar){
    ar.forEach(el => {
        if(el === ""){
            throw new Error("All fields must be filled")
        }
    })
}