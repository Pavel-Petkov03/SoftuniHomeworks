let record = null


window.addEventListener("load" , loadPage)

function loadPage (){
    const add = document.getElementsByClassName("add")[0]
    record = JSON.parse(sessionStorage.getItem("userData"))
    if(record !== null){
        document.getElementById("login").style.display = "none"
        document.getElementById("register").style.display = "none"
        add.disabled = false
    }
    add.addEventListener("click", addRecord)
    document.getElementsByClassName("load")[0].addEventListener("click" , loadRecords)
    document.getElementById("logout").addEventListener("click" ,  () => {
        try {
            generateRequest("http://localhost:3030/users/logout", "get", record.accessToken)
            sessionStorage.clear()
            window.location = "login.html"
        }
        catch (er){
            console.log("Cannot logout")
        }
    })
}

async function loadRecords(){
    let res = await fetch("http://localhost:3030/data/catches")
    let data = await res.json()
    document.getElementById("catches").replaceChildren(...data.map(el => generateComponent(el)))
}

async function addRecord(ev){
    let form = document.getElementById("addForm")
    ev.preventDefault()
    let body = new FormData(form)
    body = [...body.entries()].reduce((acc , cur) => {
        let [prop , val] = cur
        acc[prop] = val
        return acc
    }, {})
    form.reset()
    await generateRequest("http://localhost:3030/data/catches", "post" , record.accessToken ,  body)
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




function generateComponent(article){
    let isDisabled = !(article._ownerId === record.id)
    let deleteBtn = e("button" , {className : "delete" , textContent : "Delete", "data-id" : article._id, disabled : isDisabled})
    let editBtn = e("button" , {className : "update" , textContent : "Edit", "data-id" : article._id , disabled : isDisabled})
    deleteBtn.addEventListener("click" , onDelete)
    editBtn.addEventListener("click" , onEdit)
    deleteBtn.setAttribute("data-id" , article._id)
    editBtn.setAttribute("data-id" , article._id)
    return e("div", {className : "catch"}, [
        e("label" , {textContent : "Angler"}),
        e("input" , {type : "text" , className: "angler" , value : article.angler , disabled : isDisabled}),
        e("label" , {textContent : "Weight"}),
        e("input" , {type : "text" , className: "weight" , value : article.weight, disabled : isDisabled}),
        e("label" , {textContent : "Species"}),
        e("input" , {type : "text" , className: "species" , value : article.species, disabled : isDisabled}),
        e("label" , {textContent : "Location"}),
        e("input" , {type : "text" , className: "location" , value : article.location, disabled : isDisabled}),
        e("label" , {textContent : "Bait"}),
        e("input" , {type : "text" , className: "bait" , value : article.bait, disabled : isDisabled}),
        e("label" , {textContent : "Capture Time"}),
        e("input" , {type : "text" , className: "captureTime" , value : article.captureTime, disabled : isDisabled}),
        editBtn , deleteBtn
    ])
}

async function onDelete(ev){
    let id = ev.target.dataset.id
    await generateRequest(`http://localhost:3030/data/catches/${id}`, "delete" , record.accessToken)
    ev.target.parentNode.remove()
}

async function onEdit(ev){
    let body = [...ev.target.parentNode.querySelectorAll("input")].reduce((acc , cur) => {
        acc[cur.className] = cur.value
        return acc
    }, {})
    let id = ev.target.dataset.id
    await generateRequest(`http://localhost:3030/data/catches/${id}`, "put" , record.accessToken, body)
}

async function generateRequest(url , method , token , body){
    let init = {
        method,
        headers : {"content-type" : "application/json"}
    }
    if(body && Object.entries(body).length > 0){
        init.body = JSON.stringify(body)
    }
    if (token){
        init.headers["x-authorization"] = token
    }
    let res = await fetch(url, init)
    let data = await res.json()
    if(data.hasOwnProperty("message")){
        alert(data.message)
        throw new Error("server error has occurred")
    }
    return data
}



