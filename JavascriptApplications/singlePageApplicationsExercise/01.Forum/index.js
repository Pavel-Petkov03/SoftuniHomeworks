import {homePost} from "./components.js"
import {generateRequest, retrieveData, cleanData} from "../utils.js";
const topicTitleSection = document.querySelector(".topic-title")
const postsUri = "http://localhost:3030/jsonstore/collections/myboard/posts"
const [cancelBtn , postBtn] = document.getElementsByClassName("new-topic-buttons")[0]
    .querySelectorAll("button")
const form = document.getElementById("current-form")
window.addEventListener("load", async () => {
    try {
        const arrayOfPosts = await generateRequest(postsUri, "get")
        Object.values(arrayOfPosts).forEach(post => addPostToTitleSection(post))
    }catch (er){
        alert(er.message)
    }
})

cancelBtn.addEventListener("click" , (ev) => {
    ev.preventDefault()
    cleanData(form)
})

postBtn.addEventListener("click", async (ev) => {
    ev.preventDefault()
    const body = retrieveData(form)
    Object.assign(body, {"date" : new Date().toDateString()})
    try {
        const postData = await generateRequest(postsUri, "post", body)
        addPostToTitleSection(postData)
    }catch (er){
        alert(er.message)
    }
})


function addPostToTitleSection(body){
    topicTitleSection.appendChild(homePost(body))
}

