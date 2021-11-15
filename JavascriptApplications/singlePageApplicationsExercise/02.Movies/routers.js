import {registerComponent} from "./components/register.js";
import {loginComponent} from "./components/login.js";
import {footer} from "./components/footer.js"
import {navbarComponent} from "./components/navbar.js";
import {e, generateRequest} from "../utils.js";
import {homePageComponent} from "./components/homePage.js";
import {allMoviesComponent} from "./components/movies.js";
import {addMovieComponent} from "./components/addMovie.js";
import {descriptionComponent} from "./components/description.js"
import {editComponent} from "./components/edit.js";

const nav = await navbarComponent()
const registerView = registerComponent()
const footerView = footer()
const loginView = loginComponent()
const createView = addMovieComponent()
const container = document.getElementById("container")

function registerRouter(ev) {
    ev.preventDefault()
    container.replaceChildren(nav, registerView, footerView)
}

function loginRouter(ev) {
    ev.preventDefault()
    container.replaceChildren(nav, loginView , footerView)
}

async function homeRouter() {
    let addMovieBtn
    if (JSON.parse(sessionStorage.getItem("userData")) !== null) {
        addMovieBtn = e("a", {href: void (0), className: "btn btn-warning", textContent: 'Add Movie'})
        addMovieBtn.addEventListener("click", createRouter)
    }
    const arrayOfComponents = [
        nav,
        homePageComponent(),
        e("h1", {className: 'text-center', textContent: "Movies"}),
        e("section", {id: "add-movie-button"}, [
            addMovieBtn
        ]),
        await allMoviesComponent()
    ]
    arrayOfComponents.forEach(el => container.appendChild(el))
    container.appendChild(footerView)
}
function createRouter(ev){
    ev.preventDefault()
    container.replaceChildren(nav , createView, footerView)
}

async function detailsRouter(ev){
    ev.preventDefault()
    const id = ev.target.dataset.id
    try {
        const data = await generateRequest(`http://localhost:3030/data/movies/${id}`, "get")
        container.replaceChildren(nav , await descriptionComponent(data), footerView)
    }catch (er){
        alert(er.message)
    }
}

function editRouter(ev){
    ev.preventDefault()
    const title = ev.target.parentNode.parentNode.querySelector("h1").textContent.split(": ")[1]
    const img = ev.target.parentNode.parentNode.querySelector("img").src
    const description = ev.target.parentNode.querySelector("p").textContent
    const id = ev.target.parentNode.querySelector("h3").dataset.id
    container.replaceChildren(nav , editComponent({title, img , description, _id : id}), footerView)
}
export {
    registerRouter, loginRouter, homeRouter, detailsRouter, editRouter
}