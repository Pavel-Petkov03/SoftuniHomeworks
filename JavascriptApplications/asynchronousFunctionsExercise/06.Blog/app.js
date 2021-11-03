function e(type, attributes, children) {
    let element = document.createElement(type)
    if(typeof attributes === "object"){
        Object.entries(attributes).forEach(array => {
            let [prop, val] = array
            element[prop] = val
        })
    }
    if (Array.isArray(children)) {
        children.forEach(el => element.appendChild(el))
    }
    return element
}

function attachEvents() {
    document.getElementById("btnLoadPosts").addEventListener("click" , buildOptionMenu)
    document.getElementById("btnViewPost").addEventListener("click" , viewInfo)
}

async function retrieveDataByGivenEndpoint(endpoint){
    let res = await fetch(endpoint)
    return await res.json()
}

function optionComponent(id , text){
    return e("option" , {value : id , textContent : text})
}
async function buildOptionMenu(){
    let postsSelectMenu = document.getElementById("posts")
    postsSelectMenu.innerHTML = ""
    if(postsSelectMenu.children.length === 0){
        let data = await retrieveDataByGivenEndpoint("http://localhost:3030/jsonstore/blog/posts/")
        Object.entries(data).forEach(array => {
            let [id , {title}] = array
            postsSelectMenu.appendChild(optionComponent(id , title))
        })
    }
}

async function viewInfo(){
    const postsSelectMenu = document.getElementById("posts")
    const postTitle = document.getElementById("post-title")
    const postBody = document.getElementById("post-body")
    const postCommentsSection = document.getElementById("post-comments")
    postCommentsSection.innerHTML = ""
    let [{body , title} , comments ] = await Promise.all([
        retrieveDataByGivenEndpoint("http://localhost:3030/jsonstore/blog/posts/"+postsSelectMenu.value),
        retrieveDataByGivenEndpoint("http://localhost:3030/jsonstore/blog/comments")
    ])
    postTitle.textContent = title
    postBody.textContent= body

    Object.values(comments).filter((object) => object.postId === postsSelectMenu.value).forEach((value) => {
        let {text, id} = value
        postCommentsSection.appendChild(e("li", {textContent: text, id : id }))
    })
}



attachEvents();