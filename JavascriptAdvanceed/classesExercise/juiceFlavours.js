function makeBottles(array){
    let lefties = {}
    const object = array.reduce((acc , cur) => {
        let [name , quantity] = cur.split(" => ")
        const additional  = lefties[name]!== undefined ? lefties[name] : 0
        quantity = Number(quantity) + additional
        const bottles = Math.floor(quantity / 1000)
        const left = quantity % 1000
        if(left){
            lefties[name] = left
        }
        if(bottles){
            if(!acc.hasOwnProperty(name)){
                acc[name] = 0
            }
            acc[name] += bottles
        }
        return acc
    }, {})

    Object.entries(object).forEach(ar => {
        console.log(`${ar[0]} => ${ar[1]}`)
    })
}

console.log(
    makeBottles(
        ['Kiwi => 234',
            'Pear => 2345',
            'Watermelon => 3456',
            'Kiwi => 4567',
            'Pear => 5678',
            'Watermelon => 6789']
    )
)