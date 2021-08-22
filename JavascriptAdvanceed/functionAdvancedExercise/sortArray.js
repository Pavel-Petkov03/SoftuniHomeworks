function sort(array, task) {
    function ascending() {
        return array.sort((current, next) =>
            Number(current) - Number(next)
        )
    }

    function descending() {
        return array.sort((current, next) =>
            Number(next) - Number(current)
        )
    }

    switch (task) {
        case  'desc' :
            return descending()
        case  'asc' :
            return ascending()
    }
}


function typeOfArguments(...array) {
    let typesObjects = {}
    array.forEach(el => {
        console.log(typeof (el) === 'object' ? 'object:' : `${typeof (el)}: ${el}`)
        if (!(typeof (el) in typesObjects)) {
            typesObjects[typeof (el)] = 0
        }
        typesObjects[typeof (el)]++
    })
    let a = Object.entries(typesObjects).sort((first, second) => {
        return second[1] - first[1]
    })
    a.forEach(el => console.log(`${el[0]} = ${el[1]}`))
}


function getFibonator() {
    let n = 0
    let cur = 0
    let next = 0

    function increase() {
        n++
        if (n === 1) {
            next = 1;
            return 1
        }
        let temp = next
        next += cur
        cur = temp
        return next
    }

    return increase
}


function breakfastRobot(array) {
    let holderForNeeds = {
        protein : 0,
        carbohydrate : 0,
        fat : 0,
        flavour : 0
    }
    let holderForProducts = {
        apple : {carbohydrate : 1, flavour : 2},
        lemonade  : {carbohydrate : 10, flavour : 20},
        burger  : {carbohydrate : 5, flavour : 3, fat : 7},
        eggs : {flavour : 1, fat : 1, protein: 5},
        turkey : {carbohydrate : 10, flavour : 10, fat : 10 , protein : 10},
    }
    array.forEach(el => {
        el = el.split(' ')
        if (el[0] === 'report') {

        } else if (el[0] === 'restock') {
            holderForNeeds[el[1]] += el[2]
        }else{

        }
    })


    function makeOrder(meal){

    }
}
