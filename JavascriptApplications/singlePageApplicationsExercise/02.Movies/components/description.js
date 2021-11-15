import {onDelete, like, unlike, login} from "../eventListeners.js"
import {editRouter} from "../routers.js";
import {e, generateRequest} from "../../utils.js"
let userData
export async function descriptionComponent(movie){
    userData = JSON.parse(sessionStorage.getItem("userData"))
    let deleteBtn
    let editBtn
    let likeBtn
    // if user is owner of post he can't vote so I don't show the like button unlike in the picture
    if (userData._id === movie._ownerId){
        editBtn = e("a", {className : "btn btn-warning", href : void(0), textContent :"Edit"})
        deleteBtn = e("a", {className : "btn btn-danger", href : void(0), textContent :"Delete"})
        editBtn.addEventListener("click", editRouter)
        deleteBtn.addEventListener("click", onDelete)
    }else{
        likeBtn = e("a", {href : void(0)})
        try {
            const data = await generateRequest(`http://localhost:3030/data/likes`, "get")
            const filtered = data.filter(({_ownerId, movie_id}) => _ownerId === userData._id && movie_id === movie._id)
            if (filtered.length === 1){
                likeBtn.textContent = `Liked ${data.length}`
                likeBtn.addEventListener("click", unlike)
                likeBtn.className = "btn btn-success"
            }else{
                likeBtn.className = "btn btn-primary"
                likeBtn.textContent = "Like"
                likeBtn.addEventListener("click", like)
            }
        }catch (er){
            alert(er.message)
            return
        }
    }
    const h3 = e("h3", {className : "my-3", textContent: "Movie Description"})
    h3.dataset.id = movie._id
    return e("section", {id : "movie-example"}, [
        e("div", {className : "container"}, [
            e("div", {className: "row bg-light text-dark"}, [
                e("h1", {textContent : `Movie title: ${movie.title}`}),
                e("div", {className : "col-md-8"}, [
                    e("img", {className : "img-thumbnail", src : movie.img, alt : "Movie"})
                ]),
                e("div", {className : "col-md-4 text-center" ,}, [
                    h3,
                    e("p", {textContent : movie.description,  }),
                    deleteBtn,
                    editBtn,
                    likeBtn
                ])
            ])
        ])
    ])
}


