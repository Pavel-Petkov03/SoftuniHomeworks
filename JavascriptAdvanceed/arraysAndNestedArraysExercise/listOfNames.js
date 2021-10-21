function ListOfNames(array) {
    return array.sort((a, b) => a.localeCompare(b)).map((el, index) => {
        return `${index + 1}.${el}`
    }).join('\n')
}