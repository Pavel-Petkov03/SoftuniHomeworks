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
        protein: 0,
        carbohydrate: 0,
        fat: 0,
        flavour: 0
    }
    const holderForProducts = {
        apple: {carbohydrate: 1, flavour: 2},
        lemonade: {carbohydrate: 10, flavour: 20},
        burger: {carbohydrate: 5, flavour: 3, fat: 7},
        eggs: {flavour: 1, fat: 1, protein: 5},
        turkey: {carbohydrate: 10, flavour: 10, fat: 10, protein: 10},
    }

    function main(str) {
        str = str.split(' ')
        if (str[0] === 'report') {
            return `protein=${holderForNeeds.protein} carbohydrate=${holderForNeeds.carbohydrate} fat=${holderForNeeds.fat} flavour=${holderForNeeds.flavour}`
        } else if (str[0] === 'restock') {
            let [_, type, c] = str
            holderForNeeds[type] += Number(c)
            return 'Success'
        } else {
            let [_, type, c] = str
            c = Number(c)
            return makeOrder(type, c)
        }


        function makeOrder(meal, count) {
            let neededIngredients = Object.entries(holderForProducts[meal])
            for (let _ = 0; _ < count; _++) {
                for (const neededIngredient of neededIngredients) {
                    let [type, count] = neededIngredient
                    if (count > holderForNeeds[type]) {
                        return `Error: not enough ${type} in stock`
                    }
                    holderForNeeds[type] -= count
                }
            }
            return 'Success'
        }
    }

    return main
}


// see in the lecture


function add(result) {

    function main(num) {
        result += num
        return main
    }

    main.toString = () => result
    return main
}


function solution(task) {
    let rating = ''
    let allVotes = this.upvotes + this.downvotes
    let balance = this.upvotes - this.downvotes
    switch (task) {
        case 'upvote' :
            this.upvotes++;
            break
        case 'downvote' :
            this.downvotes++;
            break
        case 'score' :
            if(allVotes < 10){
                 rating = 'new'
            }
            else if (this.upvotes > allVotes * 0.66) {
                rating = 'hot'
            } else if (allVotes > 100 && balance >= 0) {
                rating = 'controversial'
            } else if (balance < 0) {
                rating = 'unpopular'
            } else {
                rating = 'new'
            }
            let final = [this.upvotes, this.downvotes, balance, rating]
            if (allVotes > 50) {
                let value = Math.ceil(Math.max(this.upvotes , this.downvotes)* 0.25)
                final[0] += value
                final[1] += value
            }
            return final
    }

}




