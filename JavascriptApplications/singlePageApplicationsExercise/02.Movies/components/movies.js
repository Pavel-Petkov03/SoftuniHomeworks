import {e, generateRequest} from "../../utils.js"
import {detailsRouter} from "../routers.js";

function oneMovie(movie){
    let button
    if (JSON.parse(sessionStorage.getItem("userData")) !== null){
        button = e("button", {className: "btn btn-info", textContent: "Details"})
        button.dataset.id = movie._id
        button.addEventListener('click', detailsRouter)
    }

    return e("div", {className : "card mb-4"}, [
        e("img", {className: "card-img-top", src : movie.img, alt : `Card image cap" width="400"`}),
        e("div", {className : "card-body"}, [
            e("h4", {className : 'card-title', textContent : movie.title})
        ]),
        e("div", {className : "card-footer"}, [
            e("a", {}, [
                button
            ])
        ])
    ])
}

export async function allMoviesComponent(){
    try {
        const data = await generateRequest("http://localhost:3030/data/movies", "get")
            return e("section", {id : "movie"}, [
                e("div", {className : "mt-3"}, [
                    e("div", {className : "row d-flex d-wrap"}, [
                        e("div", {className : "card-deck d-flex justify-content-center"}, [
                            ...data.map(oneMovie)
                        ])
                    ])
            ])
        ])
    } catch (er){
        alert(er.message)
    }
}
