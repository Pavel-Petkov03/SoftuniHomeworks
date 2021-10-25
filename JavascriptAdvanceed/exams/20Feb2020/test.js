const {assert} = require("chai")
const {numberOperations} = require("../20Feb2020/src")

describe("tests" , () => {
    describe("pow tests " , () => {
        it('should return pow of num', function () {
              assert.equal(numberOperations.powNumber(2 , 2) , 4)
            assert.equal(numberOperations.powNumber(5.12 , 2) , 26.2144)
        });
    })

    describe("number checker tests " , () => {
        describe("should throw error if invalid input ", () => {
            it('should return error', function () {
                assert.throw(() => numberOperations.numberChecker(undefined) , 'The input is not a number!')
                assert.throw(() => numberOperations.numberChecker({}) , 'The input is not a number!')
                assert.throw(() => numberOperations.numberChecker("fewfgewr") , 'The input is not a number!')
                assert.throw(() => numberOperations.numberChecker([1,2,34,]) , 'The input is not a number!')
            });
        })
        it('should return < 100 if < 100', function () {
            assert.equal(numberOperations.numberChecker(99) , 'The number is lower than 100!')
        });
        it('should return above 100 if > 100', function () {
            assert.equal(numberOperations.numberChecker(100) , 'The number is greater or equal to 100!')
            assert.equal(numberOperations.numberChecker(1000) , 'The number is greater or equal to 100!')
        });
    })
    describe("sum arrays " , () => {
        it('should return sum if two arrays equal', function () {
            assert.deepEqual(numberOperations.sumArrays([10,20,30,40] , [50,60,70,80]), [60,80, 100 , 120])
        });
        it('should return sum if two arrays not equal', function () {
            assert.deepEqual(numberOperations.sumArrays([10,20,30,40] , [50,60,70,80, 1100]), [60,80, 100 , 120, 1100])
        });

    })
})

