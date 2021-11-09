import {e, generateRequest, retrieveData} from "../utils.js"
let userData
let [create , buy , allOrders] = document.querySelectorAll("button")
function solve() {
    window.addEventListener("load" , getData)
    userData = JSON.parse(sessionStorage.getItem("userData"))
    if(userData.id){
        create.addEventListener("click" , createEvent)
        buy.addEventListener("click" ,buyEvent)
        allOrders.addEventListener("click" , allOrdersEvent)
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
        let result = await generateRequest("http://localhost:3030/data/furniture", "post" , data, userData.accessToken)
        document.querySelector("tbody").appendChild(generateTr(result))
    }catch (er){
        alert(er.message)
    }
}

async function buyEvent(){
    let body = [...document.querySelectorAll("tbody tr td input:checked")].reduce((acc , cur) => {
        let name = cur.parentNode.parentNode.querySelector('td .name').textContent
        let price = cur.parentNode.parentNode.querySelector('td .price').textContent
        acc.allOrders.push(name)
        acc.allSum += Number(price)
        return acc
    }, {allOrders : [], allSum : 0})
    document.querySelectorAll("input:checked").forEach(el => el.checked = false)
    try {
        await generateRequest("http://localhost:3030/data/orders", "post" , body , userData.accessToken)
    }
    catch (er){
        alert(er.message)
    }
}

async function allOrdersEvent(){
    let data = await generateRequest(`http://localhost:3030/data/orders/?_ownerId=${userData.id}`, "get", undefined , userData.accessToken)
    const {sum, items} = data.reduce((acc , {allOrders , allSum}) => {
        acc.sum += Number(allSum)
        allOrders.forEach(el => acc.items.add(el))
        return acc
    }, {sum : 0, items : new Set()})
    const  [priceSpan , furnitureSpan] = [...document.querySelectorAll(".all-orders-values")]
    priceSpan.textContent = sum
    furnitureSpan.textContent = [...items].join(", ")
}


function generateTr(data) {
    return e("tr", {}, [
        e("td", {}, [e("img", {src: data.img})]),
        e("td", {}, [e("p", {textContent: data.name , className : "name"}),]),
        e("td", {}, [e("p", {textContent: data.price, className : "price"})]),
        e("td", {}, [e("p", {textContent: data.factor})]),
        e("td", {}, [e("input", {type: "checkbox"})]),
    ])
}
solve()
