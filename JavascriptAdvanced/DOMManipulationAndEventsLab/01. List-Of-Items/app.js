function addItem() {
    let text = document.getElementById('newItemText').value
    let newItem = document.createElement('li')
    newItem.textContent = text
    document.getElementById('items').appendChild(newItem)
}