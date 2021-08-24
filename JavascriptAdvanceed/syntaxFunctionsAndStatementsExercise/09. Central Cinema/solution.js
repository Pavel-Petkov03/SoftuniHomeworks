function solve() {
    let onScreenButton = document.querySelector('#container button')

    onScreenButton.addEventListener('click', (ev) => {
        ev.preventDefault()
        let [name, hall, price] = ev.target.parentNode.querySelectorAll('input')
        if (name.value.length > 0 && hall.value.length > 0 && !isNaN(Number(price.value)) && price.value.length >0) {
            createNewFilm(name.value , hall.value , Number(price.value).toFixed(2))
        }
    })


    function createNewFilm(name, hall, price) {
        let li = document.createElement('li')
        let outerSpan = document.createElement('span')
        outerSpan.textContent = name
        let strong = document.createElement('strong')
        strong.textContent = `Hall: ${hall}`
        let div = document.createElement('div')
        let innerStrong = document.createElement('strong')
        innerStrong.textContent = price
        let input = document.createElement('input')
        input.placeholder = 'Tickets Sold'
        let btn = document.createElement('button')
        btn.textContent = 'Archive'
        btn.addEventListener('click' , (ev) => {
            const allTickets = ev.target.parentNode.children[1].value
            if(allTickets.length > 0 && !isNaN(Number(allTickets)) ){
                let currentLi = ev.target.parentNode.parentNode
                let ul = ev.target.parentNode.parentNode.parentNode
                ul.removeChild(currentLi)
                pushToArchive(name , (allTickets * Number(ev.target.parentNode.children[0].textContent)).toFixed(2))
            }
        })
        div.appendChild(innerStrong)
        div.appendChild(input)
        div.appendChild(btn)
        li.appendChild(outerSpan)
        li.appendChild(strong)
        li.appendChild(div)

        document.getElementById('movies').children[1].appendChild(li)
    }


    function pushToArchive(name , price){
        let li = document.createElement('li')
        let span = document.createElement('span')
        let strong = document.createElement('strong')
        let button = document.createElement('button')
        span.textContent = name
        strong.textContent = `Total amount: ${price}`
        button.textContent = 'Delete'

        button.addEventListener('click' , (ev) => {
            ev.target.parentNode.parentNode.removeChild(ev.target.parentNode)
        })
        let all = [span , strong , button]
        all.forEach(el => li.appendChild(el))
        document.getElementById('archive').children[1].appendChild(li)
    }

    document.getElementById('archive').children[2].addEventListener('click' , (ev) => {
        let ul = ev.target.parentNode.children[1]
        Array.from(ul.children).forEach(el => ul.removeChild(el))
    })
}