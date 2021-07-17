function solve() {
    let massiveOfProducts = []
    let allPrice = 0
    let arrayOfButtons = Array.from(document.querySelectorAll('.add-product'))
    let textArea = document.querySelector('textarea')
    arrayOfButtons.forEach(btn => {
        btn.addEventListener('click', (ev) => {
            const parent = ev.target.parentNode.parentNode
            const product = parent.querySelector('.product-title').textContent
            const amount = Number(parent.querySelector('.product-line-price').textContent)
            if(!massiveOfProducts.includes(product)){
                massiveOfProducts.push(product)
            }
            allPrice += amount
            textArea.value += `Added ${product} for ${amount.toFixed(2)} to the cart.\n`
        })
    })
    document.querySelector('.checkout').addEventListener('click', (ev) => {
        textArea.value += `You bought ${massiveOfProducts.join(', ')} for ${allPrice.toFixed(2)}.\n`
        Array.from(document.querySelectorAll('button')).forEach(btn => btn.disabled= true)
    })
}