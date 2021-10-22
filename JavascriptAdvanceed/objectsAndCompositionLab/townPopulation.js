let townPopulation = (array) => {
    let obj = {}
    for (let index = 0; index < array.length; index++) {
        let [key, value] = [...array[index].split(' <-> ')]
        if (!(key in obj)) {
            obj[key] = 0
        }
        obj[key] += parseInt(value)
    }
    for (const objKey in obj) {
        console.log(`${objKey} : ${obj[objKey]}`)
    }
}