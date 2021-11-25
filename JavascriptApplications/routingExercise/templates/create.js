import {html} from "../src.js"
import { generateRequest, retrieveData , getUserInfo} from "../utils.js"

const template = (create) => html`
    <div class="row space-top">
                <div class="col-md-12">
                    <h1>Create New Furniture</h1>
                    <p>Please fill all fields.</p>
                </div>
    </div>
        <form>
                <div class="row space-top">
                    <div class="col-md-4">
                        <div class="form-group">
                            <label class="form-control-label" for="new-make">Make</label>
                            <input class="form-control valid" id="new-make" type="text" name="make">
                        </div>
                        <div class="form-group has-success">
                            <label class="form-control-label" for="new-model">Model</label>
                            <input class="form-control is-valid" id="new-model" type="text" name="model">
                        </div>
                        <div class="form-group has-danger">
                            <label class="form-control-label" for="new-year">Year</label>
                            <input class="form-control is-invalid" id="new-year" type="number" name="year">
                        </div>
                        <div class="form-group">
                            <label class="form-control-label" for="new-description">Description</label>
                            <input class="form-control" id="new-description" type="text" name="description">
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="form-group">
                            <label class="form-control-label" for="new-price">Price</label>
                            <input class="form-control" id="new-price" type="number" name="price">
                        </div>
                        <div class="form-group">
                            <label class="form-control-label" for="new-image">Image</label>
                            <input class="form-control" id="new-image" type="text" name="img">
                        </div>
                        <div class="form-group">
                            <label class="form-control-label" for="new-material">Material (optional)</label>
                            <input class="form-control" id="new-material" type="text" name="material">
                        </div>
                        <input type="submit" class="btn btn-primary" value="Create" @click=${create}/>
                    </div>
                </div>
        </form>
`




export function renderCreate(ctx){
    ctx.render(template(create))
    async function create(ev){
        ev.preventDefault()
        try{
            validateFields(document.querySelectorAll(".form-group input"))
            const data = retrieveData(document.querySelector("form"))
            await generateRequest("http://localhost:3030/data/catalog", "post", data, getUserInfo().accessToken)
            ctx.redirect("/dashboard")
        }catch(er){
            alert(er.message)
        }
    }
}


function validateFields(fields){
    let isErr = false 
    for (const field of [...fields]) {
        if(validateObj[field.name](field)){
            if(field.classList.contains("is-invalid")){
                field.classList.remove("is-invalid")
            }
            field.classList.add("is-valid")
           
        }else{
            isErr = true
            if(field.classList.contains("is-valid")){
                field.classList.remove("is-valid")
            }
            field.classList.add("is-invalid")
        }
    }

    if(isErr){
        throw new Error("Invalid input")
    }
}


const validateObj = {
    "model" : (field) => field.value.length >= 4 ? true : false,
    "make" : (field) => field.value.length >= 4 ? true : false,
    "description" : (field) => field.value.length >= 10 ? true : false,
    "price" : (field) => Number(field.value) > 0 ? true : false,
    "img" : (field) => field.value.length > 0  ?true : false,
    "material" : (field) => true,
    "year" : (field) => (Number(field.value) > 1950 && Number(field.value) < 2050)  ? true : false,
}