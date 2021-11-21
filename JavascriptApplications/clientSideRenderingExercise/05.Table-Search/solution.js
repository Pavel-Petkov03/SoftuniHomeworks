import {render, html} from "https://unpkg.com/lit-html?module"
import {generateRequest} from "../utils.js";
const searchBtn = document.querySelector('#searchBtn')
const uri = "http://localhost:3030/jsonstore/advanced/table"
const searchField = document.getElementById("searchField")



async function solve() {
    searchBtn.addEventListener('click', onClick);
    function onClick(ev) {
        ev.preventDefault()
        clean()
        const searchText = searchField.value
        setClassIfMatch(searchText)
    }
    await renderData()
}



const trTemplate = (data) => html`
    <tr>
        <td>${data.firstName}${data.lastName}</td>
        <td>${data.email}</td>
        <td>${data.course}</td>
    </tr>`



async function renderData() {
    const data = await generateRequest(uri , "get")
    render(html`${Object.values(data).map(trTemplate)}`, document.querySelector("tbody"))
}


function clean(){
    document.querySelectorAll("tr").forEach(el => el.className = "")
}
function setClassIfMatch(value){
    document.querySelectorAll("tr").forEach(el => {
        if (el.textContent.toUpperCase().includes(value.toUpperCase())){
            el.className = "select"
        }
    })
}

solve()
