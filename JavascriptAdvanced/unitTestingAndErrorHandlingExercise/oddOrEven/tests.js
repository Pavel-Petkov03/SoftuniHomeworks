const {isOddOrEven} = require("../oddOrEven/oddOrEven")
const {assert} = require("chai")

describe("All tests" , () => {
    it('should return undefined if not string provided', function () {
        assert.equal(isOddOrEven([]), undefined)
        assert.equal(isOddOrEven({}), undefined)
        assert.equal(isOddOrEven(undefined), undefined)
        assert.equal(isOddOrEven(null), undefined)
        assert.equal(isOddOrEven(NaN), undefined)
        assert.equal(isOddOrEven(1), undefined)
        assert.equal(isOddOrEven(1.1), undefined)
    });

    it('should return odd if odd length of string provided', function () {
        assert.equal(isOddOrEven(""), "even")
        assert.equal(isOddOrEven("ax"), "even")
    });
    it('should return even if even length of string provided', function () {
        assert.equal(isOddOrEven("1"), "odd")
        assert.equal(isOddOrEven("123"), "odd")

    });
})