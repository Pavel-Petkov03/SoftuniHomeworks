function sameNumbers(string) {
    string = String(string)
    let list = string.split('')
    console.log(list.filter((x => x === list[0])).length === list.length ? 'true' : 'false')
    console.log(list.reduce((a, b) => (a + parseInt(b)), 0))
}