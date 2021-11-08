
const saveBtn = e("button" , {textContent : "Save"})
const submitBtn = document.getElementById("submit")
let title = document.getElementById("title")
let author = document.getElementById("author")
const formTitle = document.getElementById("form-title")
saveBtn.addEventListener("click" , async (ev) => {
    ev.preventDefault()
    const currentId =  ev.target.id
    let data = await generateRequest(`http://localhost:3030/jsonstore/collections/books/${currentId}`, "put", {
        title : title.value , author : author.value
    })
    let [currentAuthor , currentTitle] = [...document.getElementsByClassName(currentId)[0].querySelectorAll("th")]
    currentTitle.textContent = data.title
    currentAuthor.textContent = data.author
    formTitle.textContent = "FORM"
    ev.target.replaceWith(submitBtn)
    emptyFields()
})

function emptyFields(){
    title.value = ""
    author.value = ""
}

function e(type , attributes , children){
    let result = document.createElement(type)
    Object.entries(attributes).forEach(([prop , val]) => {
        result[prop] = val
    })
    if(children){
        children.forEach(el => result.appendChild(el))
    }
    return result
}


function buildTr(authorText , titleText, id){
    let deleteBtn = e("button" , {textContent : "Delete"})
    deleteBtn.addEventListener("click" , async (ev) => {
        try {
            await generateRequest("http://localhost:3030/jsonstore/collections/books/" + id, "delete")
        }catch (er){
            throw new Error("Error has occurred")
        }
        ev.target.parentNode.parentNode.remove()
    })

    const editBtn = e("button" , {textContent : "Edit"})
    editBtn.addEventListener("click" , (ev) => {
        ev.preventDefault()
        // this id is wrapped by me because it is said it's allowed
        formTitle.textContent = "Edit FORM"
        author.value = authorText
        title.value = titleText
        saveBtn.id = id
        // I hope this is allowed :)
        submitBtn.replaceWith(saveBtn)
    })
    return e("tr", {className : id }, [
        e("th", {textContent :authorText }),
        e("th", {textContent :titleText }),
        e("th", {}, [
            deleteBtn, editBtn
        ]),
    ])
}

submitBtn.addEventListener("click" , async (ev) => {
    ev.preventDefault()
    try {
        await generateRequest("http://localhost:3030/jsonstore/collections/books/",
            "post", {author : author.value , title : title.value})
        emptyFields()
    }catch (er){
        throw new Error("something went wrong")
    }
})

document.getElementById("loadBooks").addEventListener("click" , async () => {
    try{
        let data = await generateRequest("http://localhost:3030/jsonstore/collections/books/", "get", )
        let tbody = document.querySelector("tbody")
        tbody.innerHTML = ""
        Object.entries(data).forEach(([id , {author , title}]) => {
            tbody.appendChild(buildTr(author , title, id))
        })
    }catch (er){
        throw new Error("Error has occurred")
    }
})

async function generateRequest(endpoint , method , body){
    let init = {
        method : method,
        headers : {"content-type" : "application/json"},
    }
    if (body){
        init.body = JSON.stringify(body)
    }
    let res = await fetch(endpoint, init)
    return await res.json()
}