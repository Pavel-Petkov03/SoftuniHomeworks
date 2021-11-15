import {e} from "../../utils.js"
import {addMovie} from "../eventListeners.js";

export function addMovieComponent(){
    const button = e("button", {type : "submit", className : "btn btn-primary", textContent : "Submit"})
    button.addEventListener("click", addMovie)
    return e("section" , {id : "add-movie"}, [
        e("form", {className : "text-center border border-light p-5"}, [
            e("h1", {textContent : "Add Movie"}),
            e("div", {className : "form-group"}, [
                e("label", {for : "title", textContent : "Movie Title"}),
                e("input", {type : "text", className : "form-control", placeholder : "Title", name : "title"})
            ]),
            e("div", {className : "form-group"}, [
                e("label", {for : "description", textContent : "Movie Description"}),
                e("textarea", {className : "form-control", placeholder : "Description", name : "description"})
            ]),
            e("div", {className : "form-group"}, [
                e("label", {for : "imageUrl", textContent : "Image Url"}),
                e("input", {type : "text", className : "form-control", placeholder : "Image Url", name : "img", id : "imageUrl"})
            ]),
            button
        ])
    ])
}
