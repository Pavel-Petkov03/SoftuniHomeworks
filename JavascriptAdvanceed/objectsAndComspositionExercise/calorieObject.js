calorieObject = (array) => {
    let obj = {}
    for (let index = 0; index < array.length; index += 2) {
        obj[array[index]] = array[index + 1]
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
        let obj = {
            name: name,
            level: level,
            items: items === items ? items.split(', ') : []
        }
        final.push(JSON.stringify(obj))
    }
    return final
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
            console.log(`  ${array.shift()}`)
        }
    }
}


townToJson = (array) => {
    let result = []
    array.forEach((str, index, array) => array[index] = str.split(' ').join('').split('|').slice(1, -1))
    for (let index = 1; index < array.length; index++) {
        let [Town, longitude, latitude] = array[index]
        let Longitude = Number(Number(longitude).toFixed(2))
        let Latitude = Number(Number(latitude).toFixed(2))
        result.push(
            {
                Town,
                Longitude,
                Latitude
            }
        )
    }
    return JSON.stringify(result)
}
rectangle = (width, height, color) => {
    return {
        width,
        height,
        color: color[0].toUpperCase() + color.slice(1),
        calcArea(){
            return width * height
        }
    }

}

createSortedList = () => {

    let array = []
    let sortArray = (array) => {
        return array.sort((a,b) => a-b)
    }
     let obj = {
        add(element){
            array.push(element)
            array  = sortArray(array)
        },
        remove(index){
            if(index  >= 0 &&  index < array.length){
                array = array.slice(0, index) + array.slice(index+1)
                array = sortArray(array)
            }

            // Todo [make new array with popped index]
        },
        get(index){
            if(index >=0 && index < array.length){
                return array[index]
            }

        },
        size: array.length
    }
    return obj
}

solve = () => {
    return {
        fighter(name){
            let obj = {
                name,
                health : 100,
                stamina : 100
            }

        },
        mage(){

        }
    }
}


