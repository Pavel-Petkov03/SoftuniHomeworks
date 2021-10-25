function solution() {
    const input =  document.querySelector("input")
    const button = document.querySelector("button")
    const [listOfGifts , sendGifts , discardGifts] = Array.from(document.querySelectorAll(".container ul"))
    button.addEventListener("click" , () => {
        const li = createLiElement()
        console.log(li)
        listOfGifts.appendChild(li)
        const sortArray = returnSortArray()
        Array.from(listOfGifts).forEach(el => el.remove())
        sortArray.forEach(el => listOfGifts.appendChild(el))
    })

    function returnSortArray(){
        return Array.from(listOfGifts.children).sort((cur , next) => {
            return cur.textContent.localeCompare(next.textContent)
        })
    }

    function createLiElement(){
        let li = document.createElement("li")
        li.textContent = input.value
        input.value = ""
        li.classList.add("gift")
        const buttons = createButtons()
        buttons.forEach(btn => {
            li.appendChild(btn)
        })
        return li
    }

    function createButtons(){
        const arrayOfButtons = [document.createElement("button") , document.createElement("button")]
        const arrayOfClass = ["sendButton" , "discardButton"]
        const arrayOfNames = ["Send" , "Discard"]
        const arrayOfEventListeners = createEventListeners()
        arrayOfButtons.forEach((btn , index) => {
            btn.id = arrayOfClass[index]
            btn.textContent = arrayOfNames[index]
            btn.addEventListener("click" , arrayOfEventListeners[index])
        })
        return arrayOfButtons
    }

    function createEventListeners(){
        return [
            (ev) => {
                const currentLi = ev.target.parentNode
                const newLi = document.createElement("li")
                newLi.textContent = currentLi.textContent.split("SendDiscard")[0]
                sendGifts.appendChild(newLi)
                currentLi.remove()
            }, (ev) => {
                const currentLi = ev.target.parentNode
                const newLi = document.createElement("li")
                newLi.textContent = currentLi.textContent.split("SendDiscard")[0]
                discardGifts.appendChild(newLi)
                currentLi.remove()
            }
        ]
    }
}