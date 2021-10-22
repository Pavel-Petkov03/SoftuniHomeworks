function solve() {


    let headerBtn = document.getElementById('task')
    let descriptionBtn = document.getElementById('description')
    let dateBtn = document.getElementById('date')
    let addButton = document.getElementById('add')
    // eventListener for add button
    addButton.addEventListener('click', (ev) => {
        ev.preventDefault()
        let wantedDiv = getSecondDivInNeededSection(1);
        [header, description, date] = [headerBtn.value, 'Description: '+descriptionBtn.value, 'Due Date: '+dateBtn.value];
        if (validation(header, description, date)) {
            let article = createArticle([header, description, date])
            const div = createButtons(['Start', 'Delete'], ['green', 'red'])
            appendToElement(article, [div])
            appendToElement(wantedDiv, [article])
        }
    })


    // listening for click in buttons from second two last sections
    const wrapper = document.getElementsByClassName('wrapper')[0]
    wrapper.addEventListener('click', (ev) => {
        if (ev.target.nodeName === 'BUTTON' && ev.target.id !== 'add') {
            let currentSection = ev.target.parentNode.parentNode.parentNode.parentNode
            let indexOfCurrentSection = Array.from(wrapper.children).indexOf(currentSection)
            let bothButtons = Array.from(ev.target.parentNode.querySelectorAll('button'))
            let currentArticle = ev.target.parentNode.parentNode
            doCommands(ev.target, currentArticle, currentSection, getSecondDivInNeededSection(indexOfCurrentSection+1))
            if (indexOfCurrentSection === 1) {
                bothButtons.forEach(el => {
                    changePropertiesToButtons(el)
                })
            }
        }
    })

    // make validation for input fields
    function validation(header, description, date) {
        return header.length > 0 && description.length > 0 && date.length > 0
    }

    // creates article with buttons for first section
    function createArticle(arrayOfText) {
        let article = createNodeElement('article')
        let [h3, p1, p2] = [createNodeElement('h3'), createNodeElement('p'), createNodeElement('p')]
        const elements = [h3, p1, p2]
        elements.forEach((el, index) => wrapTextToNodeElement(el, arrayOfText[index]))
        appendToElement(article, elements)
        return article
    }

    // creator function for node elements [tired of typing document.createElement]
    function createNodeElement(el) {
        return document.createElement(el)
    }
    // change text to node element
    function wrapTextToNodeElement(el, text) {
        el.textContent = text
    }

    // creates a div with two buttons for first section
    function createButtons(arrayOfText, arrayOfClasses) {
        let div = createNodeElement('div')
        wrapClassToElement(div, 'flex')
        let [button1, button2] = [createNodeElement('button'), createNodeElement('button')]
        let buttonsList = [button1, button2]
        buttonsList.forEach((el, index) => {
            wrapTextToNodeElement(el, arrayOfText[index])
            wrapClassToElement(el, arrayOfClasses[index])
        })

        appendToElement(div, buttonsList)
        return div
    }

    // wrap tags in another
    function appendToElement(el, massiveOfElements) {
        massiveOfElements.forEach(node => el.appendChild(node))
    }

    // changes css classes of objects
    function wrapClassToElement(el, newClass) {
        el.className = newClass
    }

    // finds needed div in section
    function getSecondDivInNeededSection(index) {
        return document.getElementsByClassName(`wrapper`)[0].getElementsByTagName('section')[index].children[1]
    }

    // moves from current section to next one
    function moveToNextSection(article, currentSection, divInNextSection) {
        deleteArticle(article, currentSection)
        divInNextSection.appendChild(article)
    }

    // deletes article from current section
    function deleteArticle(article, currentSection){
        currentSection.querySelectorAll('div')[1].removeChild(article)
    }

    // remove the buttons for the last section
    function removeDivFromArticle(article){
        article.removeChild(article.querySelector('div'))
        return article
    }


    // change the properties of buttons in second sections
    function changePropertiesToButtons(el) {
        if (el.textContent === 'Start') {
            wrapTextToNodeElement(el, 'Delete')
            wrapClassToElement(el, 'red')
        } else {
            wrapTextToNodeElement(el, 'Finish')
            wrapClassToElement(el, 'orange')
        }
    }


    // make the logic for the buttons
    function doCommands(el, article , currentSection , nextDivInSection){
        if(el.textContent === 'Start'){
            moveToNextSection(article , currentSection , nextDivInSection)
        }else if(el.textContent === 'Delete'){
            deleteArticle(article , currentSection)
        }else{
            article = removeDivFromArticle(article)
            moveToNextSection(article, currentSection , nextDivInSection)
        }
    }
}