const {lookupChar} = require("../charLookup/charLookup")
const {assert} = require("chai")

describe("test" , () => {
    describe("should return undefined if not valid arguments" , () => {
        it('should return undefined if string is not of type string', function () {
            assert.equal(lookupChar([], 1), undefined)
            assert.equal(lookupChar({}, 1), undefined)
            assert.equal(lookupChar(1, 1), undefined)
            assert.equal(lookupChar(1.1, 1), undefined)
            assert.equal(lookupChar(null, 1), undefined)
            assert.equal(lookupChar(undefined, 1), undefined)
            assert.equal(lookupChar(NaN, 1), undefined)
        });
        it('should return undefined if index is not of type integer', function () {
            assert.equal(lookupChar("", []), undefined)
            assert.equal(lookupChar("", {}), undefined)
            assert.equal(lookupChar("", ""), undefined)
            assert.equal(lookupChar("", 1.1), undefined)
            assert.equal(lookupChar("", null), undefined)
            assert.equal(lookupChar("", undefined), undefined)
            assert.equal(lookupChar("", NaN), undefined)
        });
    })

    describe("return Incorrect index if index not in boundaries" , () => {
        it('should return Incorrect index if index is less then zero', function () {
            assert.equal(lookupChar("me" , -1) , "Incorrect index")
        });
        it('should return Incorrect index if index is more then string length', function () {
            assert.equal(lookupChar("me" , 3) , "Incorrect index")
        });
    })
    it('should return char at specific index', function () {
        assert.equal(lookupChar("pavel" , 1) , "a")
    });
})
