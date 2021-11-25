import {html, page} from "../src.js"
import { generateRequest, getUserInfo} from "../utils.js"
const template = (userId, data) => html `
        <div class="row space-top">
            <div class="col-md-12">
                <h1>Furniture Details</h1>
            </div>
        </div>
        <div class="row space-top">
            <div class="col-md-4">
                <div class="card text-white bg-primary">
                    <div class="card-body">
                        <img src="../${data.img}" />
                    </div>
                </div>
            </div>
            <form>
                <div class="col-md-4">
                    <p>Make: <span>${data.make}</span name="make"></p>
                    <p>Model: <span>${data.model}</span name="model"></p>
                    <p>Year: <span>${data.year}</span  name="year"></p>
                    <p>Description: <span>${data.description}</span  name="description"></p>
                    <p>Price: <span>${data.price}</span  name="price"></p>
                    <p>Material: <span>${data.material}</span  name="material"></p>
                    ${userId === data._ownerId ? html`<div>
                        <a href="/edit/${data._id}" class="btn btn-info" data="${data._ownerId}">Edit</a >
                        <a class="btn btn-red" href="/delete/${data._id}" data="${data._ownerId}">Delete</a>
                    </div>` : null}
                </div>
            </form>
            
        </div>
`
async function loadData(id){
    return await generateRequest(`http://localhost:3030/data/catalog/${id}`, "get")
}

export async function renderDetailsPage(ctx){
    const {_id} = getUserInfo()
    const furnitureId = ctx.params.id
    const data = await loadData(furnitureId)
    ctx.render(template(_id , data))
}