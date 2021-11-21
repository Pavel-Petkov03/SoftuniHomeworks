const uri = "http://localhost:3030/jsonstore/advanced/dropdown/"
import {generateRequest} from "../utils.js";
import {html , render} from "https://unpkg.com/lit-html?module"
const textInput = document.getElementById('itemText')
async function addItem(ev) {
    ev.preventDefault()
    const text = textInput.value
    textInput.value = ""
    await generateRequest(uri, "post", {
        text
    })
    await loadData()
}

const optionTemplate = (arrayOfOptions) => html`${arrayOfOptions.map(el => html`<option id="${el._id}">${el.text}</option>`)}`


async function loadData(){
    const data = await generateRequest(uri, "get")
    render(optionTemplate(Object.values(data)), document.getElementById("menu"))
}

document.querySelector("input[type='submit']").addEventListener("click", addItem)
loadData()