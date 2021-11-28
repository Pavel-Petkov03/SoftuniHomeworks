import { generateRequest } from "../utils.js"
import {endpoints} from "../api.js"
import {html  , until} from "../lib.js"
export const articleTemplate =  (data) => html`
 <article class="layout">
        <img src="${data.logoUrl}" class="team-logo left-col">
        <div class="tm-preview">
            <h2>${data.name}</h2>
            <p>${data.description}</p>
            <span class="details">${until(getAllNumbers(data._id), html`<p>Loading...</p>`)}</span>
            <div><a href="/details/${data._id}" class="">See details</a></div>
        </div>
    </article>
 `




async function getAllNumbers(id){
    const data = await generateRequest(endpoints.allParticipantsInTeam(id), "get")
    return data.length +1 
}
