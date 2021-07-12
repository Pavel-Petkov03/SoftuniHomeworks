calorieObject = (array) => {
    let obj = {}
    for (let index = 0; index < array.length; index += 2) {
        obj[array[index]] = parseInt(array[index + 1])
    }
    return obj
}


constructorCrew = (obj) => {
    if (obj.dizziness) {
        obj.levelOfHydrated += obj.weight * obj.experience * 0.1
        obj.dizziness = false
    }
    return obj
}

catFactory = (obj) => {
    let helperVolume = {
        90: 1800,
        120: 2400,
        200: 3500
    }
    let helperPower = (power) => {
        if (power <= 90) {
            return 90
        } else if (power <= 120) {
            return 120
        }
        return 200
    }
    let wheels = (obj) => {
        let wheelSize = Math.floor(obj.wheelsize)
        if (wheelSize % 2 === 0) {
            wheelSize--
        }
        wheelSize = Math.floor(wheelSize)
        return [wheelSize, wheelSize, wheelSize, wheelSize]
    }


    return {
        model: obj.model,
        engine: {
            power: helperPower(obj.power),
            volume: helperVolume[helperPower(obj.power)]
        },
        carriage: {
            type: obj.carriage,
            color: obj.color
        },
        wheels: wheels(obj)

    }
}
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

storageCatalogue = (array) => {
    let letter = 64
    array.sort((first, second) => {
        return first.localeCompare(second)
    })
    while (array.length > 0) {
        letter++
        let newArray = array.filter(el => el.startsWith(String.fromCharCode(letter)))
        if (newArray.length > 0) {
            console.log(String.fromCharCode(letter))
        }
        for (const el of newArray) {
            let [first, second] = array.shift().split(' : ')
            console.log(` ${first}: ${second}`)
        }
    }
}


townToJson = (array) => {

}
rectangle = (width, height, color) => {
    return {
        width,
        height,
        color: color[0].toUpperCase() + color.slice(1),
        calcArea() {
            return width * height
        }
    }

}

createSortedList = () => {

    let array = []
    let sortArray = (array) => {
        return array.sort((a, b) => a - b)
    }

    function add(element) {
        array.push(element)
        array = sortArray(array)
        this.size++
    }

    function remove(index) {
        if (index >= 0 && index < array.length) {
            array.splice(index, 1)
            this.size--
        }

    }

    function get(index) {
        if (index >= 0 && index < array.length) {
            return array[index]
        }

    }

    return {size: 0, add, remove, get}
}

solve = () => {
    return {
        fighter(name) {
            return {
                name,
                health: 100,
                stamina: 100,
                fight() {
                    this.stamina--
                    console.log(`${this.name} slashes at the foe!`)
                }
            }

        },
        mage(name) {
            return {
                name,
                health: 100,
                mana: 100,
                cast(spell) {
                    this.mana--
                    console.log(`${this.name} cast ${spell}`)
                }

            }
        }
    }
}


jansNotation = (array) => {
    let operands = ['/', '*', '+', '-']
    let numArray = []
    for (const argument of array) {
        if (operands.includes(argument)) {
            if (numArray.length >= 2) {
                let [second, first] = [numArray.pop(), numArray.pop()]
                numArray.push(eval(`${first}
                ${argument}
                ${second} `))
            } else {
                return `Error: not enough operands!`
            }
        } else {
            numArray.push(argument)
        }
    }
    if (numArray.length === 1) {
        return numArray[0]
    } else {
        return `Error: too many operands!`
    }
}


console.log(
    townToJson(
        ['| Town | Latitude | Longitude |',
            '| Veliko Turnovo | 43.0757 | 25.6172 |',
            '| Monatevideo | 34.50 | 56.11 |']
    )
)


// TODO complete townToJSON exercise