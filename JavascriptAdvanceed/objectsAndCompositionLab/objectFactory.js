const factory = (library, orders) => {
    let result = []
    for (const obj of orders) {
        let comp = Object.assign({}, obj.template)
        for (const parts of obj.parts) {
            comp[parts] = library[parts]
        }
        result.push(comp)
    }
    return result
}