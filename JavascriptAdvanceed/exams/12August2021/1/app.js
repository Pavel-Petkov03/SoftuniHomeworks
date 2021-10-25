window.addEventListener('load', solve);

function solve() {
    const addButton = document.getElementById("add")
    const model = document.getElementById("model")
    const year = document.getElementById("year")
    const description = document.getElementById("description")
    const price = document.getElementById("price")
    const tbody = document.getElementById("furniture-list")
    addButton.addEventListener("click" , (ev) => {
        ev.preventDefault()
        if(model.value !== "" && Number(year.value) > 0 && description.value !== "" && Number(price.value) > 0){
            const firstTr = createTrOne()
            const secondTr = createTrTwo()
            tbody.appendChild(firstTr)
            tbody.appendChild(secondTr)
        }
    })

    function createTrOne(){
        const tr = document.createElement("tr")
        tr.classList.add("info")
        const td1 = document.createElement("td")
        const td2 = document.createElement("td")
        const td3 = document.createElement("td")
        td1.textContent = model.value
        td2.textContent = Number(price.value).toFixed(2)
        const buttons = createTwoButtons()
        buttons.forEach(btn=> {
            td3.appendChild(btn)
        })
        let arrayOfTds = [td1 , td2 , td3]
        arrayOfTds.forEach(el => {
            tr.appendChild(el)
        })
        return tr
    }

    function createTwoButtons(){
        const classList = ["moreBtn" , "buyBtn"]
        const nameList = ["More Info" , "Buy it"]
        const eventListeners = createTwoEventListeners()
        const buttons = Array.from([document.createElement("button"), document.createElement("button")])

        buttons.forEach((btn, index ) => {
            btn.classList.add(classList[index])
            btn.addEventListener("click" , eventListeners[index])
            btn.textContent = nameList[index]
        })

        return buttons
    }

    function createTwoEventListeners(){
        const moreEventListener = (ev) => {
            const currentTr = ev.target.parentNode.parentNode
            const nextTrIndex = Array.from(tbody.children).indexOf(currentTr) + 1
            const nextTr = Array.from(tbody.children)[nextTrIndex]
            const text = ev.target.textContent
            if(text === "More Info"){
                nextTr.style.display = "contents"
                ev.target.textContent = "Less Info"
            }else{
                ev.target.textContent = "More Info"
                nextTr.style.display = "none"
            }
        }
        const buyEventListener = (ev) => {
            const currentTr = ev.target.parentNode.parentNode
            const nextTrIndex = Array.from(tbody.children).indexOf(currentTr) + 1
            const nextTr = Array.from(tbody.children)[nextTrIndex]
            const totalPrice = document.getElementsByClassName("total-price")[0]
            const currentPrice=  Number(ev.target.parentNode.parentNode.querySelectorAll("td")[1].textContent)
            totalPrice.textContent =  (currentPrice + Number(totalPrice.textContent)).toFixed(2)
            tbody.removeChild(currentTr)
            tbody.removeChild(nextTr)
        }
        return [moreEventListener , buyEventListener]
    }

    function  createTrTwo(){
        let tr = document.createElement("tr")
        tr.classList.add("hide")
        const [td1 , td2] = [document.createElement("td"), document.createElement("td")]
        td1.textContent = "Year:" + year.value
        td2.colSpan = 3
        td2.textContent = "Description:"+description.value
        tr.appendChild(td1)
        tr.appendChild(td2)

        return tr
    }
}