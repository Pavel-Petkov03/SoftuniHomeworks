import {homeRouter} from "./routers.js";
const container = document.getElementById("container")
window.addEventListener("load", async () => {
    await homeRouter()
    let movieBtn = document.querySelector("nav a")
    movieBtn.addEventListener("click", async (ev) => {
        ev.preventDefault()
        container.innerHTML = ''
        await homeRouter()
    })
})

