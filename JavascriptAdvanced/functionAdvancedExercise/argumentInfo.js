function typeOfArguments(...array) {
    let typesObjects = {}
    array.forEach(el => {
        console.log(typeof (el) === 'object' ? 'object:' : `${typeof (el)}: ${el}`)
        if (!(typeof (el) in typesObjects)) {
            typesObjects[typeof (el)] = 0
        }
        typesObjects[typeof (el)]++
    })
    let a = Object.entries(typesObjects).sort((first, second) => {
        return second[1] - first[1]
    })
    a.forEach(el => console.log(`${el[0]} = ${el[1]}`))
}
