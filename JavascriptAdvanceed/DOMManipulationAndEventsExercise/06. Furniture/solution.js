function solve() {
    let firstTextArea = document.querySelector('textarea')
    let secondTextArea = document.querySelectorAll('textarea')[1]
    document.querySelector('button').addEventListener('click', () => {
        const informationMassive = JSON.parse(firstTextArea.value)
        informationMassive.forEach(obj => {
            let img = document.createElement('img')
            let firstP = document.createElement('p')
            let secondP = document.createElement('p')
            let thirdP = document.createElement('p')
            let input = document.createElement('input')
            input.type = 'checkbox'

            let newTr = document.createElement('tr')
            let allTds = []
            for (let i = 0; i < 5; i++) {
                allTds.push(document.createElement('td'))
            }
            const appendList = [img, firstP, secondP, thirdP, input]
            allTds.forEach((el, index) => {
                el.appendChild(appendList[index])
            })
            img.src = obj.img
            firstP.textContent = obj.name
            secondP.textContent = obj.price
            thirdP.textContent = obj.decFactor
            allTds.forEach(el => newTr.appendChild(el))
            document.querySelector('tbody').appendChild(newTr)
        })

    })
    document.querySelectorAll('button')[1].addEventListener('click', () => {
        let massiveOfNames = []
        let allPay = 0
        let average = 0
        const arrayOfCheckBoxes = filterAllChecked(Array.from(document.querySelectorAll(`input`)))
        arrayOfCheckBoxes.forEach(input => {
            let parent = input.parentNode.parentNode
            let [name, price, dec] = Array.from(parent.querySelectorAll('p')).map(node => node.textContent)
            massiveOfNames.push(name)
            allPay += Number(price)
            average += Number(dec)


        })
        if(massiveOfNames.length > 0){
            const averageDec = average / arrayOfCheckBoxes.length
        secondTextArea.value = `Bought furniture: ${massiveOfNames.join(', ')}\nTotal price: ${allPay.toFixed(2)}\nAverage decoration factor: ${averageDec}`
        }

    })


    function filterAllChecked(array) {
        let newArray = []
        for (const el of array) {
            if (el.checked) {
                newArray.push(el)
            }
        }
        return newArray
    }
}