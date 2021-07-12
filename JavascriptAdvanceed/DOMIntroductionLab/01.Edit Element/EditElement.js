function editElement(element , match , replacer) {
    let mather = new RegExp(match)
    element.textContent = element.textContent.replace(mather , replacer)
}
