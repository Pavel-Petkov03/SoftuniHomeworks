function addItem() {
    let text = document.getElementById('newItemText').value
    let newItem = document.createElement('li')
    newItem.textContent = text
    let list = document.getElementById('items')
    const link = document.createElement('a')
    link.textContent = '[DELETE]'
    newItem.appendChild(link)
    link.addEventListener('click', () => {list.removeChild(link.parentNode)})
    list.appendChild(newItem)
}