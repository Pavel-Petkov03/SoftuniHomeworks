function el(type, attributes, children) {
    const el = document.createElement(type)
    Object.entries(attributes).forEach(array => {
        let [prop, value] = array
        el[prop] = value
    })
    if (Array.isArray(children)) {
        children.forEach(child => el.appendChild(child))
    }
    return el
}

function createArticlePreview(recipe) {
    let result = el("article", {className: "preview"}, [
        el("div", {className: "title"}, [el("h2", {textContent: recipe.name})]),
        el("div", {className: "small"}, [el("img", {src: recipe.img})])
    ])
    result.addEventListener("click", async () => {
        const newRecipe = await createRecipe(recipe._id)
        result.replaceWith(newRecipe)
    })
    return result
}

async function allRecipesRequest() {
    let res = await fetch("http://localhost:3030/jsonstore/cookbook/recipes")
    let data = await res.json()
    return Object.values(data)
}

async function getRecipe(id) {
    const res = await fetch(`http://localhost:3030/jsonstore/cookbook/details/${id}`)
    return await res.json()
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
    return el("article", {}, [
        el("h2", {textContent: data.name}),
        el("div", {className: "band"}, [
            el("thumb", {}, [
                el("img", {src: data.img})
            ]),
            el("div", {className: "ingredients"}, [
                el("h3", {textContent: "Ingredients:"}),
                el("ul", {}, [
                    ...data.ingredients.reduce((acc, cur) => {
                        acc.push(el("li", {textContent: cur}))
                        return acc
                    }, [])
                ])
            ])
        ]),
        el("div", {className: "description"}, [
            el("h3", {textContent: "Preparation:"}),
            ...data.steps.reduce((acc, cur) => {
                acc.push(el("p", {textContent: cur}))
                return acc
            }, [])
        ])
    ])
}


window.addEventListener("load", async () => {
    await createPreview()
})