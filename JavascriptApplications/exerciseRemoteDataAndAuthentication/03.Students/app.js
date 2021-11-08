document.getElementById("submit").addEventListener("click" , (ev) => {
    ev.preventDefault()
    let data = new FormData(document.querySelector("form"))
    let {firstName , lastName , facultyNumber , grade} = [...data.entries()].reduce((acc , cur) => {
        let [prop , val] = cur
        acc[prop] = val
        return acc
    }, {})
    if (validate([firstName , lastName , facultyNumber , grade])){
        post({firstName , lastName , facultyNumber , grade})
    }
})

function post(data){
    try {
        fetch("http://localhost:3030/jsonstore/collections/students", {
            method  : "post",
            headers :  {"content-type" : "application/json"},
            body : JSON.stringify(data)
        })
        let tbody = document.querySelector("tbody")
        tbody.appendChild(
            e("tr", {}, [
                e("th", {textContent : data.firstName}),
                e("th", {textContent : data.lastName}),
                e("th", {textContent : data.facultyNumber}),
                e("th", {textContent : data.grade}),
            ])
        )
        Array.from(document.querySelectorAll(".inputs input")).forEach(field => field.value = "")
    }catch (er){
        throw new Error("server error has occurred")
    }
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

function validate(array){
    for (const element of array) {
        if(element === "") return false
    }
    return true
}