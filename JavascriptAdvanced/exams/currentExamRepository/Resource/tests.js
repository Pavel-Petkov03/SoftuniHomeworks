const {assert} = require("chai")
const library = require("../Resource/library")

describe("all Tests", () => {
    describe("all tests for price" , () => {
        it('should throw error if name or year are not good types', function () {
            assert.throw(() => library.calcPriceOfBook(1, 1), "Invalid input")
            assert.throw(() => library.calcPriceOfBook("", ""), "Invalid input")
            assert.throw(() => library.calcPriceOfBook(null, ""), "Invalid input")
            assert.throw(() => library.calcPriceOfBook(undefined, ""), "Invalid input")
            assert.throw(() => library.calcPriceOfBook(null, 1), "Invalid input")
            assert.throw(() => library.calcPriceOfBook(null, 1), "Invalid input")
            assert.throw(() => library.calcPriceOfBook([], 1), "Invalid input")
            assert.throw(() => library.calcPriceOfBook( "", []), "Invalid input")
        });
        it('should return 50 percent off if 1980 or less', function () {
            let expected = `Price of name is 10.00`
            assert.equal(library.calcPriceOfBook("name" , 1980), expected)
            assert.equal(library.calcPriceOfBook("name" , 1979), expected)
        });
        it('should return all price if above 1980', function () {
            let expected = `Price of name is 20.00`
            assert.equal(library.calcPriceOfBook("name" , 1981), expected)
        });
    })
    describe("findBook" , () => {
        it('should throw error if empty array', function () {
            assert.throw(() => library.findBook([], ""), "No books currently available")
        });

        it('should return book if presented ', function () {
            let expected = "We found the book you want."
            assert.equal(library.findBook(["name"], "name"), expected)
        });
        it('should return  not found if not found', function () {
            let expected = "The book you are looking for is not here!"
            assert.equal(library.findBook(["nam"], "name"), expected)
        });
    })
    describe("arrange the books" , () => {
        it('should throw error if invalid input', function () {
            assert.throw(() => library.arrangeTheBooks(""), "Invalid input")
            assert.throw(() => library.arrangeTheBooks(-1), "Invalid input")
        });
        it('should return great job if current Books to 40', function () {
            let expected = "Great job, the books are arranged.";
            assert.equal(library.arrangeTheBooks(40), expected)
            assert.equal(library.arrangeTheBooks(39), expected)
        });
        it('should return baf if above 40', function () {
            let expected = "Insufficient space, more shelves need to be purchased.";
            assert.equal(library.arrangeTheBooks(41), expected)
        });
    })
})