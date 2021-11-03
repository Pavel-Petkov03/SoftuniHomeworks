class ChristmasDinner {
    constructor(budget) {
        this.budget = budget
        this.guests = {}
        this.dishes = []
        this.products = []
    }

    get budget() {
        return this._budget
    }

    set budget(value) {
        if (value < 0) {
            throw new Error("The budget cannot be a negative number")
        }
        this._budget = value
    }

    shopping(productArray) {
        const [product, price] = productArray
        if (this.budget >= price) {
            this.products.push(product)
            this.budget -= price
            return `You have successfully bought ${product}!`
        }
        throw new Error("Not enough money to buy this product")
    }

    recipes(recipe) {
        const {recipeName, productsList} = recipe
        for (const product of productsList) {
            if(!this.products.includes(product)){
                throw new Error( "We do not have this product")
            }
        }
        this.dishes.push({recipeName , productsList})
        return `${recipeName} has been successfully cooked!`
    }

    inviteGuests(name, dish){
        if(!this.dishes.reduce((acc , cur) => {acc.push(cur.recipeName) ; return acc}, []).includes(dish)){
            throw new Error("We do not have this dish")
        }
        if(this.guests.hasOwnProperty(name)){
            throw new Error("This guest has already been invited")
        }
        this.guests[name] = dish
        return `You have successfully invited ${name}!`
    }

    showAttendance(){
        return Object.entries(this.guests).reduce((acc , cur) => {
            const [name , dish] = cur
            const filter = this.dishes.filter(el => el.recipeName === dish )
            acc.push(`${name} will eat ${dish}, which consists of ${filter[0].productsList.join(", ")}`)
            return acc
        }, []).join("\n")
    }
}

let dinner = new ChristmasDinner(300);

dinner.shopping(['Salt', 1]);
dinner.shopping(['Beans', 3]);
dinner.shopping(['Cabbage', 4]);
dinner.shopping(['Rice', 2]);
dinner.shopping(['Savory', 1]);
dinner.shopping(['Peppers', 1]);
dinner.shopping(['Fruits', 40]);
dinner.shopping(['Honey', 10]);

dinner.recipes({
    recipeName: 'Oshav',
    productsList: ['Fruits', 'Honey']
});
dinner.recipes({
    recipeName: 'Folded cabbage leaves filled with rice',
    productsList: ['Cabbage', 'Rice', 'Salt', 'Savory']
});
dinner.recipes({
    recipeName: 'Peppers filled with beans',
    productsList: ['Beans', 'Peppers', 'Salt']
});

dinner.inviteGuests('Ivan', 'Oshav');
dinner.inviteGuests('Petar', 'Folded cabbage leaves filled with rice');
dinner.inviteGuests('Georgi', 'Peppers filled with beans');

console.log(dinner.showAttendance());
