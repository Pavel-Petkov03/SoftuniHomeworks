const {isSymmetric} = require("../second/checkForSymmetry")
const {assert} = require("chai")
describe("Tests", () => {
    it('should return false if non array provided', function () {
        assert.equal(isSymmetric(false), false)
        assert.equal(isSymmetric(null), false)
        assert.equal(isSymmetric({}), false)
        assert.equal(isSymmetric(0), false)
        assert.equal(isSymmetric(0.1), false)
        assert.equal(isSymmetric(true), false)
        assert.equal(isSymmetric(undefined), false)
    });

    it('should return true if symmetric', function () {
        assert.equal(isSymmetric([1, 23, 1]), true)
    });
    it('should return false if two different types in function', function () {
        assert.equal(isSymmetric([1, 23, "1"]), false)
    });
})


function playingCards(face, suit) {
    const validFace = ["2", "3" , "4", "5", "6", "7", "8", "9", "10", "J" , "K" , "Q" , "A"]
    const suits = {
        "S" : "\u2660",
        "H" : "\u2665 ",
        "D" : "\u2666 ",
        "C" : "\u2663 ",
    }
    if(!Object.keys(suits).includes(suit) || !validFace.includes(face)){
        throw new Error("This card in invalid")
    }
    return `${face}${suits[suit]}`
}

function printDeckOfCards(cards) {
    function createCard (face , suit){
        const validFace = ["2", "3" , "4", "5", "6", "7", "8", "9", "10", "J" , "K" , "Q" , "A"]
        const suits = {
            "S" : "\u2660",
            "H" : "\u2665 ",
            "D" : "\u2666 ",
            "C" : "\u2663 ",
        }
        if(!Object.keys(suits).includes(suit) || !validFace.includes(face)){
            throw new Error(`${face}${suit}`)
        }
        return `${face}${suits[suit]}`
    }
    try{
        console.log(cards.reduce((acc , cur) => {
            const [face , suit] = [cur.slice(0,-1) , cur.slice(-1)]
            const newCard = createCard(face , suit)
            acc.push(newCard)
            return acc
        }, []).join(" "))
    }catch (er){
       console.log(`Invalid card: ${er.message}`)
    }
}