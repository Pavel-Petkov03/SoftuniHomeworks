import {generateRequest, retrieveData} from "../utils.js";
import {commentOnCommentSection, postOnCommentSection} from "../01.Forum/components.js"
const commentsUri = "http://localhost:3030/jsonstore/collections/myboard/comments/"
const postUri = "http://localhost:3030/jsonstore/collections/myboard/posts/"
const id = sessionStorage.getItem("id")
const commentSection = document.querySelector(".comment")
window.addEventListener("load", async () => {
    try {
        const [postData , commentData] = await Promise.all([
            generateRequest(postUri + id , "get"),
            generateRequest(commentsUri, "get")
        ])
        commentSection.appendChild(postOnCommentSection(postData))
        const postComments = Object.values(commentData).filter(obj => obj.postId === id)
        // The api is object object structure so I can't use query params in comment get request
        postComments.forEach(comment => commentSection.appendChild(commentOnCommentSection(comment)))
    }catch (er){
        er.message
    }
})

const button = document.querySelector("button")

button.addEventListener("click", async(ev) => {
    ev.preventDefault()
    const data = retrieveData(document.querySelector("form"))
    Object.assign(data , {date : new Date().toDateString(), postId : id})
    try {
        const comment = await generateRequest(commentsUri , "post" , data)
        commentSection.appendChild(commentOnCommentSection(comment))
    }catch (er){
        alert(er.message)
    }
})