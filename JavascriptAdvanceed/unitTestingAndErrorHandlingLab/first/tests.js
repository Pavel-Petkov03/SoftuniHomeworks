
const {assert} = require("chai")
const {sum} = require("../first/sumOfNumbers")
describe('array', function () {
    it('should return sum when array provided', function () {
        assert.equal(sum([1, 2, 3, 4, 5]), 15)
    });

    it('should return 0 when empty array', function () {
        assert.equal(sum([]), 0)
    });
});