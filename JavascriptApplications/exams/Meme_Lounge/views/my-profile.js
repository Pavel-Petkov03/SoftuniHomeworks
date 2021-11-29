import {html , } from "../lib.js"
import { generateRequest, getUserInfo } from "../utils.js"


const template = (userData , memes) => html`
    ${console.log(userData)}
    <section id="user-profile-page" class="user-profile">
            <article class="user-info">
                <img id="user-avatar-url" alt="user-profile" src="/images/${userData.gender}.png">
                <div class="user-content">
                    <p>Username: ${userData.username}</p>
                    <p>Email: ${userData.email}</p>
                    <p>My memes count: ${memes.length}</p>
                </div>
            </article>
            <h1 id="user-listings-title">User Memes</h1>
            <div class="user-meme-listings">
                <!-- Display : All created memes by this user (If any) --> 
                ${memes.length !==0 ?  memes.map(userMemeTemplate)  :  html` <p class="no-memes">No memes in database.</p>`}
                <!-- Display : If user doesn't have own memes  --> 
            </div>
        </section>
`

const userMemeTemplate = (data) => html`
    <div class="user-meme">
        <p class="user-meme-title">${data.title}</p>
        <img class="userProfileImage" alt="meme-img" src="${data.imageUrl}">
        <a class="button" href="/details/${data._id}">Details</a>
        </div>
`

export async function renderMyProfile(ctx){
    const [userData , memes] = await retrieveUserInfo()
    ctx.render(template(userData , memes))
}

async function retrieveUserInfo(){
    const {username, email , _id, gender} = getUserInfo()
    const memes = await generateRequest(`http://localhost:3030/data/memes?where=_ownerId%3D%22${_id}%22&sortBy=_createdOn%20desc`)
    return [{username , email , _id, gender} , memes]
}

