import {generateRequest, e} from "../utils.js";

function createArticlePreview(recipe) {
    let result = e("article", {className: "preview"}, [
        e("div", {className: "title"}, [e("h2", {textContent: recipe.name})]),
        e("div", {className: "small"}, [e("img", {src: recipe.img})])
    ])
    result.addEventListener("click", async () => {
        const newRecipe = await createRecipe(recipe._id)
        result.replaceWith(newRecipe)
    })
    return result
}

async function allRecipesRequest() {
    try {
        let data = await generateRequest("http://localhost:3030/data/recipes/", "get")
        return Object.values(data)
    } catch (er) {
        alert(er.message)
    }
}

async function getRecipe(id) {
    try {
        let data = await generateRequest(`http://localhost:3030/data/recipes/${id}`, "get")
        return data
    } catch (er) {
        alert(er.message)
    }
}

async function createPreview() {
    const main = document.getElementsByTagName("main")[0]
    main.innerHTML = ""
    const data = await allRecipesRequest()
    data.forEach(el => {
        main.appendChild(createArticlePreview(el))
    })
}

async function createRecipe(id) {
    const data = await getRecipe(id)
    return e("article", {}, [
        e("h2", {textContent: data.name}),
        e("div", {className: "band"}, [
            e("thumb", {}, [
                e("img", {src: data.img})
            ]),
            e("div", {className: "ingredients"}, [
                e("h3", {textContent: "Ingredients:"}),
                e("ul", {}, [
                    ...data.ingredients.reduce((acc, cur) => {
                        acc.push(e("li", {textContent: cur}))
                        return acc
                    }, [])
                ])
            ])
        ]),
        e("div", {className: "description"}, [
            e("h3", {textContent: "Preparation:"}),
            ...data.steps.reduce((acc, cur) => {
                acc.push(e("p", {textContent: cur}))
                return acc
            }, [])
        ])
    ])
}

function authenticateUser(){
    // here is no endpoint for authenticating person on backed so I just authenticate session storage
    let data = JSON.parse(sessionStorage.getItem("userData"))
    if(data && data.hasOwnProperty("accessToken")){
        document.getElementById("guest").style.display = "none"
    }else{
        document.getElementById("user").style.display = "none"
    }
}


window.addEventListener("load", async () => {
    await createPreview()
    authenticateUser()
    document.getElementById("logoutBtn").addEventListener("click" , logout)
    // I changes a little the css file in order to show the proper buttons for user or guest
})

