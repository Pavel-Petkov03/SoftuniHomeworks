class Restaurant{
    constructor(budget) {
        this.budgetMoney = budget
        this.menu = {}
        this.stockProducts = {}
        this.history = []
    }

    loadProducts(array){
        return array.reduce((acc , product) => {
            let [name , quantity , allPrice] = product.split(" ")
            quantity = Number(quantity)
            allPrice = Number(allPrice)
            if(this.budgetMoney >= allPrice){
                this.history.push(`Successfully loaded ${quantity} ${name}`)
                acc.push(`Successfully loaded ${quantity} ${name}`)
                this.budgetMoney -= allPrice
                if(!this.stockProducts.hasOwnProperty(name)) {
                    this.stockProducts[name] = 0
                }
                this.stockProducts[name] += quantity
                return acc
            }
            this.history.push(`There was not enough money to load ${quantity} ${name}`)
            acc.push(`There was not enough money to load ${quantity} ${name}`)
            return acc
        }, []).join("\n")
    }

    addToMenu(meal , neededProducts , price){
        if(this.menu.hasOwnProperty(meal)){
            return `The ${meal} is already in the our menu, try something different.`
        }
        this.menu[meal] = {
            price,
            neededProducts : neededProducts.reduce((acc , cur) => {
                let [name , price] = cur.split(" ")
                acc[name] = Number(price)
                return acc
            }, {})
        }
        if(Object.keys(this.menu).length === 1){
            return `Great idea! Now with the ${meal} we have 1 meal in the menu, other ideas?`
        }
        return `Great idea! Now with the ${meal} we have ${Object.keys(this.menu).length} meals in the menu, other ideas?`
    }

    showTheMenu(){
        if(Object.keys(this.menu).length === 0){
            return "Our menu is not ready yet, please come later..."
        }
        return Object.entries(this.menu).reduce((acc , cur) => {
            const [meal , object] = cur
            acc.push(`${meal} - $ ${object.price}`)
            return acc
        }, []).join("\n")
    }

    makeTheOrder(meal){
        if(!this.menu.hasOwnProperty(meal)){
            return `There is not ${meal} yet in our menu, do you want to order something else?`
        }
        const currentMeal = this.menu[meal]
        for (const currentMealElement of Object.entries(currentMeal.neededProducts)) {
            let [name , price] = currentMealElement
            if(!(this.stockProducts.hasOwnProperty(name) && this.stockProducts[name] >= price)){
                return `For the time being, we cannot complete your order (${meal}), we are very sorry...`
            }
        }
        Object.entries(currentMeal.neededProducts).forEach(product => {
            let [name , price] = product
            this.stockProducts[name] -= price
        })
        this.budgetMoney += currentMeal.price
        return `Your order (${meal}) will be completed in the next 30 minutes and will cost you ${currentMeal.price}.`
    }
}
let kitchen = new Restaurant(1000);
kitchen.loadProducts(['Yogurt 30 3', 'Honey 50 4', 'Strawberries 20 10', 'Banana 5 1']);
kitchen.addToMenu('frozenYogurt', ['Yogurt 1', 'Honey 1', 'Banana 1', 'Strawberries 10'], 9.99);
console.log(kitchen.makeTheOrder('frozenYogurt'));
