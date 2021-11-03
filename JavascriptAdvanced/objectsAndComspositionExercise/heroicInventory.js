heroicInventory = (array) => {
    let final = []
    for (let index = 0; index < array.length; index++) {
        let [name, level, items] = array[index].split(' / ')
        level = Number(level)
        items = items ? items.split(', ') : []

        final.push({name, level, items})
    }
    console.log(JSON.stringify(final))
}