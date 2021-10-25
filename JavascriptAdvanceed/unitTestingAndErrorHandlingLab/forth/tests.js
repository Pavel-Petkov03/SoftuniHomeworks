const {createCalculator} = require("../forth/createCalculator")
const {assert} = require("chai")

describe("tests for createCalculator" , () => {

    it('should return value if get function invoked', function () {
        const calc = createCalculator()
        const expect = 0
        assert.equal(calc.get() , expect)
    });
    it('should add value if add invoked', function () {
        const calc = createCalculator()
        calc.add("100")
        const expect = 100
        assert.equal(calc.get() , expect)
    });
    it('should subtract value if subtract function invoked', function () {
        const calc = createCalculator()
        calc.subtract("100")
        const expect = -100
        assert.equal(calc.get() , expect)
    });
    it('should subtract value if subtract function invoked', function () {
        const calc = createCalculator()
        calc.subtract(100)
        calc.add(100)
        const expect = 0
        assert.equal(calc.get() , expect)
    });
    it('check for properties', function () {
        const calc = createCalculator()
        assert.isTrue(calc.hasOwnProperty("add"))
        assert.isTrue(calc.hasOwnProperty("subtract"))
        assert.isTrue(calc.hasOwnProperty("get"))
    });

    it('should return valid number if two adds', function () {
        const calc = createCalculator()
        calc.add("10")
        calc.add("10")
        assert.equal(calc.get() , 20)
    });
})
