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
function composePeople(object){
    const main = document.getElementById("main")
    main.innerHTML = ""
    Object.values(object).map(el => composePerson(el)).forEach(profile => main.appendChild(profile))
}

function composePerson(person){
    let div = e("div" , {id : person._id}, [
        e("h3"),
        e("label",  {textContent : "Email"}),
        e("input",  {type : "text", value : person.email, disabled : true , readOnly : true }),
        e("label",  {textContent : "Age"}),
        e("input",  {type : "text", value : person.age, disabled : true , readOnly : true }),
    ])
    const button = e("button" , {textContent : "Show More"})
    const unlockProfileRadio = e("input",  {type : "radio", value : "unlock", name : person._id})


    let el = e("div" , {className : "profile"}, [
        e("img" , {src : "./iconProfile2.png", className: "userIcon"}),
        e("label",  {textContent : "Lock"}),
        e("input",  {type : "radio", value : "lock", checked : true , name : person._id}),
        e("label",  {textContent : "Unlock"}),
        unlockProfileRadio,
        e("h3"),
        e("label",  {textContent : "Username"}),
        e("input",  {type : "text", value : person.username, disabled : true , readOnly : true }),
        div,
        button
    ])
    button.addEventListener("click" , (ev) => {
        let currentDiv = document.getElementById(person._id)
        if(unlockProfileRadio.checked){
            if(currentDiv.style.display === "none"){
                ev.target.textContent = "Show More"
                currentDiv.style.display = "block"
            }else{
                ev.target.textContent = "Show Less"
                currentDiv.style.display = "none"
            }
        }
    })

    return el
}

async function lockedProfile() {
    let data = await takePeople()
    composePeople(data)
}

async function takePeople(){
    let res = await fetch("http://localhost:3030/jsonstore/advanced/profiles")
    return await res.json()
}