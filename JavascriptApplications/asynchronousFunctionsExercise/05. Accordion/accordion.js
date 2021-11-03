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

function component(person){
    let button = e("button" , {id : person._id, textContent: "More", className : "button"})
    let firstDiv = e("div" , {className : "head"}, [
        e("span" , {textContent : person.title}),
        button
    ])

    let extraDiv = e("div" , {className: "extra"} )
    button.addEventListener("click" , async(ev) => {
        if(ev.target.textContent === "More"){
            if(extraDiv.children.length === 0){
                let currentId = ev.target.id
                let data = await retrieveDataByGivenEndpoint(`http://localhost:3030/jsonstore/advanced/articles/details/${currentId}`)
                extraDiv.appendChild(e("p", {textContent : data.content}))
            }
            ev.target.textContent = "Less"
        }else{
            ev.target.textContent = "More"
        }
        extraDiv.classList.toggle("extra")
    })

    return e("div" , {className : "accordion"}, [
        firstDiv, extraDiv
    ])
}

async function solution() {
    let data = await retrieveDataByGivenEndpoint("http://localhost:3030/jsonstore/advanced/articles/list")
    let main = document.getElementById("main")
    main.innerHTML = ""
    data.map(el => component(el)).forEach(el => main.appendChild(el))
}

async function retrieveDataByGivenEndpoint(endpoint){
    let res = await fetch(endpoint)
    return await res.json()
}

solution()