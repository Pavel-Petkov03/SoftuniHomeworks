import { generateRequest , getUserInfo} from "../utils.js"


export async function renderDelete(ctx){
    const id = ctx.params.id
    try{
        await generateRequest(`http://localhost:3030/data/catalog/${id}`, "delete", undefined , getUserInfo().accessToken)
        ctx.redirect("/dashboard")
    }catch(er){
        alert(er.message)
    }
}