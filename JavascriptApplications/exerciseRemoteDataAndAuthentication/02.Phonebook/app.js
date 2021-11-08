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
            await fetch("http://localhost:3030/jsonstore/phonebook/"+_id, {
                method : "delete",
                "content-type" : "application-json",
            })
            ev.target.parentNode.remove()
        })
        li.appendChild(deleteBtn)
        ul.appendChild(li)
    })
}

function post(ev){
    ev.preventDefault()
    let person = document.getElementById("person")
    let phone = document.getElementById("phone")
    fetch("http://localhost:3030/jsonstore/phonebook/", {
        method : "post",
        headers : {"content-type" : "application/json"} ,
        body : JSON.stringify({
            person: person.value , phone : phone.value
        })
    })

    person.value = ""
    phone.value = ""
}
attachEvents();