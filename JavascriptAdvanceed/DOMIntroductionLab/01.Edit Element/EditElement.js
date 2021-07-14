function editElement(element , match , replacer) {
    let mather = new RegExp(match, 'g')
    element.textContent = element.textContent.replace(mather , replacer)
}
