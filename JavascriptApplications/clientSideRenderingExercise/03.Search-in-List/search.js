import {render, html} from "https://unpkg.com/lit-html?module"
import {towns} from "./towns.js";

const template = (arrayOfTowns) => html`<ul>${arrayOfTowns.map(el => html`<li>${el}</li>`)}</ul>`
const input = document.getElementById("searchText")


function search(ev) {
    ev.preventDefault()
    const searchText = input.value
    clearPreviousState()
    Array.from(document.querySelectorAll("li")).forEach(el => {
        if (el.textContent.toUpperCase().includes(searchText.toUpperCase())){
            el.className = "active"
        }
    })
}
function clearPreviousState(){
    Array.from(document.querySelectorAll("li")).forEach(el => el.className = "")
}
render(template(towns), document.getElementById("towns"))
document.querySelector("button").addEventListener("click", search)