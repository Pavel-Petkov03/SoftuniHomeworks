import {e, generateRequest, retrieveData} from "../utils"


document.getElementById("submit").addEventListener("click" , async (ev) => {
    ev.preventDefault()
    let {firstName , lastName , facultyNumber , grade} = retrieveData(document.querySelector("form"))
    if (validate([firstName , lastName , facultyNumber , grade])){
        await post({firstName , lastName , facultyNumber , grade})
    }
})

async function post(data){
    try {
        await generateRequest("http://localhost:3030/jsonstore/collections/students", "post", data)
        let tbody = document.querySelector("tbody")
        tbody.appendChild(generateComponent(data))
        Array.from(document.querySelectorAll(".inputs input")).forEach(field => field.value = "")
    }catch (er){
        throw new Error("server error has occurred")
    }
}

function generateComponent(data){
    return e("tr", {}, [
        e("th", {textContent : data.firstName}),
        e("th", {textContent : data.lastName}),
        e("th", {textContent : data.facultyNumber}),
        e("th", {textContent : data.grade}),
    ])
}

function validate(array){
    for (const element of array) {
        if(element === "") return false
    }
    return true
}