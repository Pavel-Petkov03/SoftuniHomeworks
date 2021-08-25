function solve() {
    const addButton = document.getElementById('add')
    addButton.addEventListener('click', (ev) => {
        ev.preventDefault()
        let task = document.getElementById('task').value
        let description = document.getElementById('description').value
        let date = document.getElementById('date').value
        if (task.length > 0 && description.length > 0 && date.length > 0) {
            let newArticle = createArticleWithContent(task, description, date)
            createButtonsToArticle(newArticle, ['Start', 'Delete'], ['green', 'red'])
            let currentDiv = returnNeededDivInSection(1)
            appendAllElementsToNodeElement(currentDiv, [newArticle])
        }
    })

    let openButtons = Array.from(document.querySelector('.wrapper').children[1].querySelector('button'))
    openButtons.forEach(btn => {
        if (btn.value === 'Start') {
            btn.value = 'Delete'
            let article = 1
        } else {

        }
    })


    function createElement(el) {
        return document.createElement(el)
    }

    function wrapTextToNodeElement(el, text) {
        el.textContent = text
    }

    function createArticleWithContent(header, description, dueDate) {
        let article = createElement('article')
        let h3 = createElement('h3')
        let p1 = createElement('p')
        let p2 = createElement('p2')


        let fieldsOfElements = [h3, p1, p2]
        let fieldsOfText = [header, description, dueDate]
        fieldsOfElements.forEach((el, index) => wrapTextToNodeElement(el, fieldsOfText[index]))

        appendAllElementsToNodeElement(article, fieldsOfElements)
        return article
    }


    function createButtonsToArticle(article, textMassive, classMassive) {
        let div = createElement('div')
        changeClassToElement(div, 'flex')


        let button1 = createElement('button')
        let button2 = createElement('button')
        let buttonsList = [button1, button2]

        buttonsList.forEach((el, index) => {
            wrapTextToNodeElement(el, textMassive[index])
            changeClassToElement(el, classMassive[index])
        })
        const eventsMassive = [startEventListener, deleteEventListener]
        buttonsList.forEach((el, index) => attachEventListener(el, eventsMassive[index]))

        appendAllElementsToNodeElement(div, buttonsList)
        appendAllElementsToNodeElement(article, [div])
    }

    function changeClassToElement(el, newClass) {
        el.classList.add(newClass)
    }


    function appendAllElementsToNodeElement(el, massive) {
        massive.forEach(node => el.appendChild(node))
    }

    function returnNeededDivInSection(index) {
        return document.querySelector('.wrapper').getElementsByTagName('section')[index].childNodes[1]
    }


    function attachEventListener(el, eventFunction) {
        el.addEventListener('click', eventFunction)
    }

    function startEventListener(ev) {
        let article = ev.target.parentNode.parentNode
        let section = ev.target.parentNode.parentNode.parentNode.parentNode
        deleteArticle(ev, article)
        const index = Array.from(document.querySelector('.wrapper').children).indexOf(section)
        let newDiv = returnNeededDivInSection(index + 1)
        console.log(newDiv)
        console.log(article)
        newDiv.appendChild(article)
    }

    function deleteEventListener(ev) {

        deleteArticle(ev, ev.target.parentNode.parentNode)
    }

    function deleteArticle(ev, article) {
        let div = ev.target.parentNode.parentNode.parentNode
        div.removeChild(article)
    }
}