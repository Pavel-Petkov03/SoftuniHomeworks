const {mathEnforcer} = require("../mathEnforcer/mathEnforcer")
const {assert} = require("chai")

describe("tests" , () => {
    describe("addFive" , () => {
        it('should return undefined if not number provided', function () {
            assert.equal(mathEnforcer.addFive(undefined), undefined)
            assert.equal(mathEnforcer.addFive(null), undefined)
            assert.equal(mathEnforcer.addFive(""), undefined)
            assert.equal(mathEnforcer.addFive([]), undefined)
            assert.equal(mathEnforcer.addFive({}), undefined)
        });
        it('should return num + 5 if integer provided', function () {
            assert.equal(mathEnforcer.addFive(5) , 10)
            assert.equal(mathEnforcer.addFive(-5) , 0)
        });

        it('should return num + 5 if float provided', function () {
            assert.closeTo(mathEnforcer.addFive(1.001), 6, 0.01)
            assert.closeTo(mathEnforcer.addFive(-5.0003) , 0, 0.01)
        });
    })
    describe("subtractTen" , () => {
        it('should return undefined if not number provided', function () {
            assert.equal(mathEnforcer.subtractTen(undefined), undefined)
            assert.equal(mathEnforcer.subtractTen(null), undefined)
            assert.equal(mathEnforcer.subtractTen(""), undefined)
            assert.equal(mathEnforcer.subtractTen([]), undefined)
            assert.equal(mathEnforcer.subtractTen({}), undefined)
        });

        it('should return num + 10 if integer provided', function () {
            assert.equal(mathEnforcer.subtractTen(5) , -5)
            assert.equal(mathEnforcer.subtractTen(-5) , -15)
        });

        it('should return num + 10 if float provided', function () {
            assert.closeTo(mathEnforcer.subtractTen(1.001), -9, 0.01)
            assert.closeTo(mathEnforcer.subtractTen(-1.001), -11, 0.01)
            assert.closeTo(mathEnforcer.subtractTen(-12.123), -22.12, 0.01)
            assert.closeTo(mathEnforcer.subtractTen(17.1), 7.1 , 0.01)
        });
    })

    describe("sumTwo" , () => {
        describe('test numbers undefined' , () => {
            it('should return undefined if first number not correct type',  () => {
                assert.equal(mathEnforcer.sum(undefined, 1), undefined)
                assert.equal(mathEnforcer.sum(null, 1), undefined)
                assert.equal(mathEnforcer.sum("", 1), undefined)
                assert.equal(mathEnforcer.sum([], 1), undefined)
                assert.equal(mathEnforcer.sum({}, 1), undefined)
            });
            it('should return undefined if first second not correct type',  () => {
                assert.equal(mathEnforcer.sum(1,undefined), undefined)
                assert.equal(mathEnforcer.sum(1,null), undefined)
                assert.equal(mathEnforcer.sum(1,""), undefined)
                assert.equal(mathEnforcer.sum(1,[]), undefined)
                assert.equal(mathEnforcer.sum(1,{}), undefined)
            });
        })

        it('should return sum of two integers', function () {
            assert.equal(mathEnforcer.sum(5,5) , 10)
            assert.equal(mathEnforcer.sum(10,20) , 30)
            assert.equal(mathEnforcer.sum(-5,5) , 0)
        });

        it('should return num  if float provided', function () {
            assert.closeTo(mathEnforcer.sum(1.001, 1), 2, 0.01)
            assert.closeTo(mathEnforcer.sum(1.001, 1.001), 2, 0.01)
            assert.closeTo(mathEnforcer.sum(1.001, 0.00000012), 1.00, 0.01)
            assert.closeTo(mathEnforcer.sum(-1, -12.0303), -13.03, 0.01)
            assert.closeTo(mathEnforcer.sum(-1, -12.0303), -13.03, 0.01)
            assert.closeTo(mathEnforcer.sum(1.001, -0.00000012), 1.00, 0.01)
            assert.closeTo(mathEnforcer.sum(-1.01, 13), 12, 0.01)
            assert.closeTo(mathEnforcer.sum(-1.1, 13), 11.9, 0.01)
            assert.closeTo(mathEnforcer.sum(1.001, -0.00000012), 1.00, 0.01)
            assert.closeTo(mathEnforcer.sum(-12.123, -10), -22.12, 0.01)
            assert.closeTo(mathEnforcer.sum(-0.1, -0.2), -0.3, 0.01)
        });
    })
})
