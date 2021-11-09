import {generateRequest} from "../utils"

function attachEvents() {
    document.getElementById("btnCreate").addEventListener("click" , post)
    document.getElementById("btnLoad").addEventListener("click" , get)
}
async function get(){
    let res = await fetch("http://localhost:3030/jsonstore/phonebook/")
    let data = await res.json()
    build(data)
}

function build(data){
    let ul = document.getElementById("phonebook")
    Object.values(data).forEach(({person , phone, _id}) => {
        const li = document.createElement("li")
        li.textContent = `${person}: ${phone}`
        let deleteBtn = document.createElement("button")
        deleteBtn.textContent = "Delete"
        deleteBtn.addEventListener("click" , async (ev) => {
            try {
                await generateRequest("http://localhost:3030/jsonstore/phonebook/"+_id, "delete")
            }
            catch (er){
                alert(er.message)
            }
            ev.target.parentNode.remove()
        })
        li.appendChild(deleteBtn)
        ul.appendChild(li)
    })
}

async function post(ev){
    ev.preventDefault()
    let person = document.getElementById("person")
    let phone = document.getElementById("phone")
    try {
        await generateRequest("http://localhost:3030/jsonstore/phonebook/", "post", {
            person : person.value, phone : phone.value
        })
    }catch (er){
        alert(er.message)
    }
    person.value = ""
    phone.value = ""
}
attachEvents();