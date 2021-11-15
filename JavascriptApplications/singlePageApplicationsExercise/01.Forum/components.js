import {e} from "../utils.js"

function homePost(post){
    const aTag = e("a" , {href : "theme-content.html", className : "normal"}, [
        e("h2" , {textContent : post.topicName})
    ])
    aTag.addEventListener("click", () => sessionStorage.setItem("id", post._id))
    return e("div" , {className : "topic-container", id : post._id}, [
        e("div" , {className : "topic-name-wrapper"}, [
            e("div" , {className : "topic-name"}, [
                aTag,
                e("div" , {className : "columns"}, [
                    e("div" , {}, [
                        e("p" , {textContent : `Date:`}, [
                            e("time", {textContent : post.date})
                        ]),
                        e("div", {className : "nick-name"}, [
                            e("p", {textContent : "Username:"}, [
                                e("span", {textContent : post.username})])
                        ])
                    ])
                ])
            ])
        ])
    ])
}
function postOnCommentSection(post){
    return e("div",  {className :"header"}, [
        e("img" , {src : './static/profile.png', alt : "avatar"}),
        e("p",  {}, [
            e("span", {textContent : `${post.username} posted on`}, [
                e("time" , {textContent : post.date})
            ])
        ]),
        e("p" , {className : "post-content", textContent : post.postText})
    ])
}

function commentOnCommentSection(comment){
    return e("div", {id : comment._id}, [
        e("div" , {className : "topic-name-wrapper"}, [
            e("div" , {className : 'topic-name'}, [
                e("p" , {innerHTML : `<strong>${comment.username}</strong> commented on <time>${comment.date}</time>`}),
                e("div" , {className : "post-content"}, [
                    e("p" , {textContent : comment.postText})
                ])
            ])
        ])
    ])
}


export {
    homePost,
    postOnCommentSection,
    commentOnCommentSection
}