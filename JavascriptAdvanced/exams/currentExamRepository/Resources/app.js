window.addEventListener('load', solve);

function solve() {
    let [genre, name , author , date ] = Array.from(document.querySelectorAll("input"))
    const addBtn = document.getElementById("add-btn")
    const savedContainer = Array.from(document.getElementsByClassName("saved-container"))[0]
    console.log(savedContainer)
    const likeP = Array.from(document.getElementsByClassName("likes"))[0].querySelector("p")
    const allHitsContainer = Array.from(document.getElementsByClassName("all-hits-container"))[0]
    addBtn.addEventListener("click" , (ev) => {
        ev.preventDefault()
        if(genre.value !== "" && name.value  && author.value && date.value){
            const div = createDiv(genre.value,name.value, author.value , date.value)
            allHitsContainer.appendChild(div)
            const ar = [genre , name , author , date ]
            ar.forEach(el => el.value = "")
        }
    })

    function  createDiv(genreName , nameName , authorName, dateName){
        let div = document.createElement("div")
        div.classList.add("hits-info")
        let htwo1 = document.createElement("h2")
        let htwo2 = document.createElement("h2")
        let htwo3 = document.createElement("h2")
        let h3 = document.createElement("h3")
        const img = document.createElement("img")
        img.src = "./static/img/img.png"
        htwo1.textContent = "Genre :" + genreName
        htwo2.textContent = "Name :" + nameName
        htwo3.textContent = "Author :" + authorName
        h3.textContent = "Date : " + dateName
        const ar = [img , htwo1, htwo2, htwo3, h3, ]
        const buttonArray = createButtons()
        ar.forEach(el => div.appendChild(el))
        buttonArray.forEach(el => div.appendChild(el))
        return div
    }


    function  createButtons(){
        let [saveBtn , likeBtn, deleteBtn] = [document.createElement("button"),document.createElement("button"),document.createElement("button")]
        const arrayOfClasses = ["save-btn" , "like-btn" , "delete-btn"]
        const arrayOfEvent = returnArrayOfEventListeners()
        const ar = [saveBtn , likeBtn , deleteBtn]
        const arrayOfNames = ["Save song", "Like song" , "Delete"]
        ar.forEach((el, index) => {
            el.classList.add(arrayOfClasses[index])
            el.addEventListener("click" , arrayOfEvent[index])
            el.textContent = arrayOfNames[index]
        })
        return ar

    }
    function  returnArrayOfEventListeners(){
        function  save(ev){
            const parent = ev.target.parentNode.parentNode
            const currentDiv = ev.target.parentNode
            const saveBtn = currentDiv.querySelector(".save-btn")
            const likeBtn = currentDiv.querySelector(".like-btn")
            saveBtn.remove()
            likeBtn.remove()
            savedContainer.appendChild(currentDiv)
            parent.removeChild(currentDiv)
        }

        function  like(ev){
            ev.target.disabled = true
            const [text , num] = likeP.textContent.split(": ")
            likeP.textContent = `${text}: ${Number(num) + 1}`
        }

        function  deleteBtn(ev){
            const currentDiv = ev.target.parentNode
            currentDiv.remove()
        }

        return [save , like , deleteBtn]
    }
}