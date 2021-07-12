function extractText() {
    let listOfLiElements = [...document.getElementsByTagName('li')]
    listOfLiElements.forEach((el , index , array) => array[index] = el.textContent)

    let textArea = document.getElementById('result')
    textArea.textContent = listOfLiElements.join('\n')
}