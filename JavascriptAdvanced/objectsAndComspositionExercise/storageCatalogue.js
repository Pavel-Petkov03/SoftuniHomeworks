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