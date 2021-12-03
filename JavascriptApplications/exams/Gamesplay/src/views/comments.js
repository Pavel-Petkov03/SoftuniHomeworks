import { html , page} from "../lib.js";
import { endpoints } from "../api.js";
import { generateRequest, getUserInfo } from "../utils.js";


const commentTemplate = (data) => html`
    <li class="comment">
        <p>Content: ${data.comment}</p>
    </li>
`



async function postComment(gameId , ev){
    ev.preventDefault()
    const textarea = document.querySelector("textarea")
    const comment = textarea.value
    await generateRequest(endpoints.postComments, "post" , {
        gameId, comment
    }, getUserInfo().accessToken)
    page.redirect(`/details/${gameId}`)
    textarea.value = ''
}

async function getAllComments(id){
    return await generateRequest(endpoints.comments(id) , "get")
}

export {
    postComment, getAllComments, commentTemplate
}