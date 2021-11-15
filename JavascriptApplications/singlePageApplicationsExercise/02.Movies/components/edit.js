import {edit} from "../eventListeners.js"
import {e} from "../../utils.js"

export function editComponent(movie){
    const editBtn = e("button", {type : "submit", className : "btn btn-primary", textContent : "Submit"})
    editBtn.dataset.id = movie._id
    editBtn.addEventListener("click", edit)
    return e("section", {id : "edit-movie"}, [
        e("form", {className : "text-center border border-light p-5", action : void(0)}, [
            e("h1", {textContent : "Edit Movie"}),
            e("div", {className: "form-group"}, [
                e("label", {for : "title", textContent: "Movie Title"}),
                e("input", {className : "form-control", id: "title", type : "text", value : movie.title, name : 'title'})
            ]),
            e("div", {className: "form-group"}, [
                e("label", {for : "description", textContent: "Movie Description"}),
                e("input", {className : "form-control", id: "description", type : "text", value : movie.description, name : 'description'})
            ]),
            e("div", {className: "form-group"}, [
                e("label", {for : "imageUrl", textContent: "Image url"}),
                e("input", {className : "form-control", id: "imageUrl", type : "text", value : movie.img, name : "img"})
            ]),
            editBtn
        ])
    ])
}