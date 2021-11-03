lowestPricesInCities = (array) => {
    let result = []
    for (let index = 0; index < array.length; index++) {
        let [town, product, i] = array[index].split(' | ')
        let price = Number(i)
        let sameObject = result.filter(obj => obj.product === product)
        if (sameObject.length > 0) {
            if (sameObject.price > price) {
                sameObject.price = price
            }
        } else {
            result.push({town, price, product})
        }

    }
    result.forEach((el, index) => result[index] = `${el.product} -> ${el.price} (${el.town})`)
    return result.join('\n')
}