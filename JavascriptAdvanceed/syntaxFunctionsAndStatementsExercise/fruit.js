function fruit(string, grams, price) {
    grams /= 1000
    console.log(`I need $${(price * grams).toFixed(2)} to buy ${grams.toFixed(2)} kilograms ${string}.`)
}
