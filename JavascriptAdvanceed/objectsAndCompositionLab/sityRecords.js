let cityRecords = (name, population, treasury) => {
    return {
        name, population, treasury
    }
}

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

let cityTaxes = (name, population, treasury) => {
    return {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.population * this.taxRate
        },
        applyGrowth(percentage) {
            this.population += Math.floor(this.population * percentage / 100)
        },
        applyRecession(percentage) {
            this.treasury -= Math.ceil(this.treasury * percentage / 100)
        }

    }
}


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


createAssemblyLine = () => {
    return {
        hasClima(obj) {
            obj.temp = 21
            obj.tempSettings = 21
            obj.adjustTemp = function () {
                if (obj.temp > obj.tempSettings) {
                    obj.temp--
                } else if (obj.tempSettings > obj.temp) {
                    obj.temp++
                }
            }
        },
        hasAudio(track) {
            track.currentTrack = {
                name: null,
                artist: null
            }
            track.nowPlaying = function () {
                if (track.currentTrack.name !== null && track.currentTrack.artist !== null) {
                    console.log(`Now playing '${track.currentTrack.name}' by ${track.currentTrack.artist}`)
                }
            }
        },
        hasParktronic(object) {
            object.checkDistance = function (distance) {
                let result = ''
                if (distance < 0.1) {
                    result = "Beep! Beep! Beep!"
                } else if (distance < 0.25) {
                    result = "Beep! Beep!"
                } else if (distance < 0.5) {
                    result = "Beep!"
                }
                console.log(result)
            }
        }
    }
}

function serializeData(json) {
    let objectArray = JSON.parse(json)
    let matrix = [Object.keys(objectArray[0])]
    objectArray.forEach(array => matrix.push(Object.values(array)))
    const closeTag = (tag) => {
        tag = tag.split('')
        return [tag[0], '/', ...tag.slice(1)].join('')
    }
    matrix[0] = '<tr>' + matrix[0].map(el => `<th>${el}${closeTag('<th>')}`).join('') + '</tr>'
    for (let index = 1; index < matrix.length; index++) {
        matrix[index] = '<tr>' + matrix[index].map(el => `<td>${el}${closeTag('<td>')}`).join('') + '</tr>'
    }
    matrix.forEach((el, index) => matrix[index]=`   ${el}`)
    matrix.unshift('<table>')
    matrix.push('</table>')
    return matrix.join('\n')

}

// TODO
// make corrections on json exercise [make clear logic not hardcoded]
console.log(
    serializeData(
        '[{"Name":"Stamat", "Score":5.5}, {"Name":"Rumen", "Score":6}]'
    )
)