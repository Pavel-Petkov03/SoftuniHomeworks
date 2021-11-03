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