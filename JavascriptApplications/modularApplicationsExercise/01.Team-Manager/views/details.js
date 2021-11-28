// TODO 
// make decorator for error handling and endpoints for error messages
// combine the themplates below in one template

import {html, page} from "../lib.js"
import { generateRequest, getUserInfo } from "../utils.js"
import {endpoints} from "../api.js"
import { handleModal } from "./modal.js"
const loggedUserTemplate = (data , status , members, currentUserId) => html`
    <section id="team-home">
                <article class="layout">
                    <img src="${data.logoUrl}" class="team-logo left-col">
                    <div class="tm-preview">
                        <h2>${data.name}</h2>
                        <p>Gotta catch 'em all!</p>
                        <span class="details">${members.length} Members</span>
                        <div>
                            ${status === "pending" ?  html`Membership pending. <a href="#" @click=${removeAndLeave.bind(null , data._id, currentUserId)}>
                            Cancel request</a>` : status === "member" ?  html`<a href="#" class="action invert" 
                            @click=${removeAndLeave.bind(null , data._id, currentUserId)}>Leave team</a>` : html`<a href="/details/${data._id}" class="action" @click=${join.bind(null , data._id)}>Join team</a>`} 
                        </div>
                    </div>
                    <div class="pad-large">
                        <h3>Members</h3>
                        <ul class="tm-members">
                            ${members.map(el => ownerMembersTemplate(el , false))}
                        </ul>
                    </div>
                </article>
            </section>
`


const ownerTemplate = (data, members , pending) => html`
    <section id="team-home">
                <article class="layout">
                    <img src="${data.logoUrl}" class="team-logo left-col">
                    <div class="tm-preview">
                        <h2>${data.name}</h2>
                        <p>Gotta catch 'em all!</p>
                        <span class="details">${members.length}</span>
                        <div>
                            <a href="/edit/${data._id}" class="action">Edit team</a>
                        </div>
                    </div>
                    <div class="pad-large">
                        <h3>Members</h3>
                        <ul class="tm-members">
                            ${members.map(el => ownerMembersTemplate(el , true))}
                        </ul>
                    </div>
                    <div class="pad-large">
                        <h3>Membership Requests</h3>
                        <ul class="tm-members">
                            ${pending.map(el => ownerGuestTemplate(el , true))}
                        </ul>
                    </div>
                </article>
            </section>
`

const guestTemplate = (data , members) => html`
<section id="team-home">
                <article class="layout">
                    <img src="${data.logoUrl}" class="team-logo left-col">
                    <div class="tm-preview">
                        <h2>${data.name}</h2>
                        <p>Gotta catch 'em all!</p>
                        <span class="details">${members.length} Members</span>
                    </div>
                    <div class="pad-large">
                        <h3>Members</h3>
                        <ul class="tm-members">
                            ${members.map(el => ownerMembersTemplate(el , false))}
                        </ul>
                    </div>
                </article>
            </section>
`

const ownerMembersTemplate = (data, isOwner) => 
html`<li>${data.user.username}${isOwner ? html`<a class="tm-control action" 
@click=${decline.bind(null , data.teamId, data._ownerId)}>Remove from team</a>` : null}</li>`



const ownerGuestTemplate = (data, isOwner) => 
html`<li>${data.user.username}${isOwner ? html`<a  class="tm-control action" 
@click=${approve.bind(null , data.teamId, data._ownerId)}>Approve</a><a href="#"class="tm-control action" 
@click=${decline.bind(null , data.teamId, data._ownerId)}>Decline</a>` : null}</li>`



async function decline(teamId , userId , ev){
    ev.preventDefault()
    handleModal("Do you realy want to remove the user" , true , true , async () => {
        const [{_id}] = await generateRequest(endpoints.findPersonInParticularTeam(teamId , userId), "get")
        await generateRequest(endpoints.currentMember(_id), "delete" , null , getUserInfo().accessToken)
        page.redirect(`/details/${teamId}`)
    })
}



async function getTeamInfo(teamId){
    return await generateRequest(endpoints.currentTeam(teamId), "get")
}

async function approve(teamId , userId, ev){
    ev.preventDefault()
    handleModal("Do you realy want to approve the user" , true , true , async () => {
        const [{_id}] = await generateRequest(endpoints.findPersonInParticularTeam(teamId , userId), "get")
        await generateRequest(endpoints.currentMember(_id), "put", {
            status : "member"
        },  getUserInfo().accessToken)
        page.redirect(`/details/${teamId}`)
    })
}

async function join(teamId , ev){
    ev.preventDefault()
    handleModal("Do you want to join this team" , true , true , async () => {
        await generateRequest(endpoints.allPeopleInAllTeams, "post", {
            teamId,
            status : "pending"
        }, getUserInfo().accessToken)
        page.redirect(`/details/${teamId}`)
    })
}
async function removeAndLeave(teamId , userId , ev){
    ev.preventDefault()
    handleModal("Do you want to leave the team", true , true , async() => {
        await generateRequest(endpoints.currentMember(userId) , "delete", null , getUserInfo().accessToken)
        page.redirect(`/details/${teamId}`)
    })
}

export async function renderDetails(ctx){
    let currentUserId = getUserInfo()
    const teamId = ctx.params.id
    const data = await getTeamInfo(teamId)
    const allMembers = await generateRequest(endpoints.queryMembersByKey(teamId , "member"), "get")
    if(currentUserId === null){
        return ctx.render(guestTemplate(data , allMembers))
    }
    else if(currentUserId._id === data._ownerId){
        const allPending = await generateRequest(endpoints.queryMembersByKey(teamId , "pending"), "get")
        ctx.render(ownerTemplate(data , allMembers , allPending))
    }else {
        let userData = await generateRequest(endpoints.findPersonInParticularTeam(teamId , currentUserId._id), "get")
        let status
        let id 
        if(userData.length === 0){
            status = undefined
        }else{
            status = userData[0].status
            id = userData[0]._id
        }
        ctx.render(loggedUserTemplate(data , status , allMembers, id))
    }
}