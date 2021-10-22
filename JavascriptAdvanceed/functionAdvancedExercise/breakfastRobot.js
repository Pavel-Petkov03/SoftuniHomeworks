
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