function  autoEngineeringCompany(array){
    const object = array.reduce((acc , cur) => {
        const [model , brand, count ] = cur.split(" | ")
        if(!acc.hasOwnProperty(model)){
            acc[model] = {}
        }
        if(!acc[model].hasOwnProperty(brand)){
            acc[model][brand] = 0
        }
        acc[model][brand] += Number(count)
        return acc
    }, {})
    return Object.entries(object).forEach((model) => {
        const [name, objectBrand] = model
        console.log(name)
        Object.entries(objectBrand).forEach(brand => console.log(`###${brand[0]} -> ${brand[1]}`))
    })
}

console.log(autoEngineeringCompany(
    ['Audi | Q7 | 1000',
        'Audi | Q6 | 100',
        'BMW | X5 | 1000',
        'BMW | X6 | 100',
        'Citroen | C4 | 123',
        'Volga | GAZ-24 | 1000000',
        'Lada | Niva | 1000000',
        'Lada | Jigula | 1000000',
        'Citroen | C4 | 22',
        'Citroen | C5 | 10']

))