import {render, html} from "https://unpkg.com/lit-html?module"
import {cats} from "./catSeeder.js";
const liTemplate = (data) => html`
    <li>
        <img src="./images/${data.imageLocation}.jpg" width="250" height="250" alt="Card image cap">
        <div class="info">
            <button class="showBtn" @click="${loadStatusCode}">Show status code</button>
            <div class="status" style="display: none" id=${data.id} >
                <h4>Status Code: ${data.statusCode}</h4>
                <p>${data.statusMessage}</p>
            </div>
        </div>
    </li>
`



const ulTemplate = (arrayOfLi) => html`<ul>${arrayOfLi.map(liTemplate)}</ul>`


function loadStatusCode(ev){
    const div = ev.target.parentNode.querySelector(".status")
    const state = div.style.display
    if ( state === "none"){
        div.style.display = "block"
        ev.target.textContent = "Hide status Code"
    }else{
        ev.target.textContent = "Show status Code"
        div.style.display = "none"
    }
}
function renderData(){
    render(ulTemplate(cats), document.getElementById("allCats"))
}

renderData()