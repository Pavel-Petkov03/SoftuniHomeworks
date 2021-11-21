import {render, html} from "https://unpkg.com/lit-html?module"
import {generateRequest, retrieveData} from "../utils.js"
let addForm = document.querySelector("form")
const uri = "http://localhost:3030/jsonstore/collections/books/"
document.getElementById("loadBooks").addEventListener("click", getAllBooks)
document.querySelector("input[value='Submit']").addEventListener("click", submit)
const tbody = document.querySelector("tbody")
let editForm

async function getAllBooks(){
    try {
        const books = await generateRequest(uri , "get")
        const modifiedBooks = Object.entries(books).reduce((acc , cur) => {
            const [key , {author , title}] = cur
            acc.push({_id : key , author , title})
            return acc
        }, [])
        render(html`${modifiedBooks.map(el => tableRowTemplate(el))}`, tbody)
    }catch (er){
        alert(er.message)
    }
}


function editEvent(data , ev){
    ev.preventDefault()
    render(editFormTemplate(data), document.querySelector("body"))
    editForm = document.querySelector("#edit-form")
    toggleSections(addForm, editForm)
    hideEdit(true)
    document.querySelector("input[value='Save']").addEventListener("click", save)
}

async function save(ev){
    ev.preventDefault()
    const id = ev.target.parentNode.querySelector("input").id
    const body = retrieveData(editForm)
    try {
        await generateRequest(uri+id, "put", body)
        toggleSections(editForm, addForm)
        hideEdit(false)
        await getAllBooks()
    }catch (er){
        alert(er.message)
    }
}

function hideEdit(bool){
    Array.from(document.querySelectorAll("button")).filter(el => {
        if (el.textContent === "Edit"){
            el.disabled = bool
        }
    })
}

function toggleSections(hide , show){
    hide.style.display = "none"
    show.style.display = "block"
}

async function submit(ev){
    ev.preventDefault()
    const body = retrieveData(addForm)
    if (Object.values(body).every(el => el !== "")){
        try {
            await generateRequest(uri , "post", body)
            await getAllBooks()
        }catch (er){
            alert(er.message)
        }
    }
}

async function deleteEvent(data , ev){
    const {_id} = data
    ev.preventDefault()
    try {
        await generateRequest(uri+_id, "delete")
        ev.target.parentNode.parentNode.remove()
    }catch (er){
        alert(er.message)
    }
}

const editFormTemplate = (data) => html`
    <form id="edit-form">
        <input type="hidden" id="${data._id}">
        <h3>Edit book</h3>
        <label>TITLE</label>
        <input type="text" name="title" value=${data.title}>
        <label>AUTHOR</label>
        <input type="text" name="author" value=${data.author}>
        <input type="submit" value="Save">
    </form>
`


const tableRowTemplate = (data) => html`
    <tr>
        <td>${data.title}</td>
        <td>${data.author}</td>
        <td>
            <button @click="${editEvent.bind(null , data)}">Edit</button>
            <button @click="${deleteEvent.bind(null , data)}">Delete</button>
        </td>
    </tr>`