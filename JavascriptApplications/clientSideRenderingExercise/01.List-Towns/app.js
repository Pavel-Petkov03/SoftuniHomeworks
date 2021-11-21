import {html, render} from "https://unpkg.com/lit-html?module"

const ulTemplate  = (data) => html`<ul>${data.map(el => html`<li>${el}</li>`)}</ul>`

function renderData(ev){
    ev.preventDefault()
    const root = document.getElementById("root")
    const input = document.getElementById("towns")
    const array = input.value.split(", ")
    render(ulTemplate(array), root)
    input.value = ""
}


document.getElementById("btnLoadTowns").addEventListener("click", renderData)




