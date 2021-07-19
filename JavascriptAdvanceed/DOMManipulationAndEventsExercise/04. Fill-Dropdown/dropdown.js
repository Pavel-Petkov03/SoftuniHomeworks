function addItem() {
    let valueField = document.getElementById('newItemValue')
    let textField = document.getElementById('newItemText')
    let newOption = document.createElement('option')
    newOption.textContent = textField.value
    newOption.value = valueField.value
    document.getElementById('menu').appendChild(newOption)
    valueField.value = ''
    textField.value = ''

}