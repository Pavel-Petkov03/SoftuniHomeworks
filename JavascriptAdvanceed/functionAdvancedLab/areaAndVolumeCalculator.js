function solve(area, vol, input) {
    let array = JSON.parse(input)
    let finalArray = []
    array.forEach(obj => {
        finalArray.push(
            {
                area: area.call(obj),
                volume: vol.call(obj)
            }
        )
    })

    return finalArray
}


function vol() {
    return Math.abs(this.x * this.y * this.z);
}


function area() {
    return Math.abs(this.x * this.y);
}
