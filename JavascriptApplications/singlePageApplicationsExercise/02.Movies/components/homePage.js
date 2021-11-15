import {e} from "../../utils.js"
export function homePageComponent() {
    return e("section" , {id : "home-page"}, [
        e("div", {className : "jumbotron jumbotron-fluid text-light\" style=\"background-color: #343a40;"},[
            e("img" , {
                src : "https://slicksmovieblog.files.wordpress.com/2014/08/cropped-movie-banner-e1408372575210.jpg",
                className : "img-fluid",
                alt : "Responsive image" ,
                style : "width: 150%; height: 200px"
            }),
            e("h1" , {className : "display-4", textContent : "Movies"}),
            e("p", {className : "lead", textContent : "Unlimited movies, TV shows, and more. Watch anywhere. Cancel anytime."})
        ])
    ])
}