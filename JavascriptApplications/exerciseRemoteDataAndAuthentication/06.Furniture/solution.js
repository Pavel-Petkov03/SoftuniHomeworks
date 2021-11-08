import {e, generateRequest, retrieveData} from "../utils.js"
let token
let [create , buy , allOrders] = document.querySelectorAll("button")
function solve() {
    window.addEventListener("load" , getData)
    token = sessionStorage.getItem("userData")
    if(token){
        create.addEventListener("click" , createEvent)
    }else{
        [...document.getElementsByClassName("authorized")].forEach(el => el.style.display = "none")
    }
}

async  function getData(){
    let data =  await generateRequest("http://localhost:3030/data/furniture" , "get")
    document.querySelector("tbody").replaceChildren(...data.map(el => generateTr(el)))
}

async function createEvent(ev){
    ev.preventDefault()
    let data = retrieveData(document.querySelector("form"))
    try {
        await generateRequest("http://localhost:3030/data/furniture", "post" , data, token)
    }catch (er){
        alert(er.message)
    }
    // todo make component
}

function buyEvent(){

}

function generateTr(data) {
    return e("tr", {}, [
        e("td", {}, [e("img", {src: data.img})]),
        e("td", {}, [e("p", {textContent: data.name}),]),
        e("td", {}, [e("p", {textContent: data.price})]),
        e("td", {}, [e("p", {textContent: data.factor})]),
        e("td", {}, [e("input", {type: "checkbox"})]),
    ])
}

solve()
