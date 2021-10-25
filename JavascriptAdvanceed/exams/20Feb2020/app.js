function solve() {
    const [creator, title, category] = Array.from(document.querySelectorAll("input"))
    const content = document.getElementById("content")
    const ol = document.querySelector("ol")
    const button = document.getElementsByClassName("btn create")[0]
    const appendSection = document.querySelector("main section")
    button.addEventListener("click" , (ev) => {
        ev.preventDefault()
        const article = createArticle(category.value , creator.value , title.value , content.value)
        appendSection.appendChild(article)
    })
    function createArticle(categoryText , creatorText , titleText, contentText ) {
        let article = document.createElement("article")
        let h1 = document.createElement("h1")
        let p1 = document.createElement("p")
        let p2 = document.createElement("p")
        let p3 = document.createElement("p")
        let strong1 = document.createElement("strong")
        strong1.textContent = categoryText
        let strong2 = document.createElement("strong")
        strong2.textContent = creatorText
        h1.textContent = titleText
        p1.textContent = "Category: "
        p2.textContent = "Creator: "
        p1.appendChild(strong1)
        p2.appendChild(strong2)
        p3.textContent = contentText
        const div = document.createElement("div")
        div.classList.add("buttons")
        const arrayOfButtons = createButtons()
        arrayOfButtons.forEach(el => {
            div.appendChild(el)
        })
        const appendElementList = [h1 ,p1 , p2 , p3 , div]
        appendElementList.forEach(el => article.appendChild(el))
        return article
    }

    function createButtons(){
        const arrayOfButtons = [document.createElement("button"), document.createElement("button")]
        const classList = ["delete" , "archive"]
        const nameList = ["Delete" , "Archive"]
        const eventList = createEventListeners()
        arrayOfButtons.forEach((btn , index) => {
            btn.textContent = nameList[index]
            btn.addEventListener("click" , eventList[index])
            btn.classList.add("btn")
            btn.classList.add(classList[index])
        })
        return arrayOfButtons
    }

    function createEventListeners(){
        function deleteListener(ev){
            const article = ev.target.parentNode.parentNode
            article.remove()
        }
        function archiveListener(ev){
            const article = ev.target.parentNode.parentNode
            const h1 = article.querySelector("h1")
            const li = document.createElement("li")
            li.textContent = h1.textContent
            ol.appendChild(li)
            const newArray = sortSection()
            ol.innerHTML = ""
            newArray.forEach(el => ol.appendChild(el))
            article.remove()
        }
        return [deleteListener , archiveListener]
    }

    function sortSection(){
        return Array.from(ol.children).sort((cur , next) => {
            return cur.textContent.localeCompare(next.textContent)
        })
    }
}