const cinema = require("./code")
const {assert} = require("chai")

describe("All tests ", () => {
    describe("Show movies" , () => {
        it('should return message if array length === 0', function () {
            const message = 'There are currently no movies to show.'
            const actual = cinema.showMovies([])
            assert.equal(actual , message)
        });
        it('should join array if more than one element provided', function () {
            const actual = cinema.showMovies([1,2,3,4])
            assert.equal(actual , "1, 2, 3, 4")
        });
    })

    describe("Ticket price" , () => {
        describe("Test hasOwnPropertyWitAllFields" , () => {
            it('should return price of premiere', function () {
                const expected = 12.00
                const actual = cinema.ticketPrice("Premiere")
                assert.equal(actual , expected)
            });
            it('should return price of Normal', function () {
                const expected = 7.5
                const actual = cinema.ticketPrice("Normal")
                assert.equal(actual , expected)
            });
            it('should return price of Discount', function () {
                const expected = 5.5
                const actual = cinema.ticketPrice("Discount")
                assert.equal(actual , expected)
            });
        })
        it('should raise error if invalid type provided', function () {
            assert.throw(() => cinema.ticketPrice("mama"))
            try{
                cinema.ticketPrice("mama")
            }catch (err){
                assert.equal(err.message , 'Invalid projection type.')
            }
        });
    })
    describe("swapSeatsInHall" , () => {
        describe("Invalid input" , () => {
            it('should return error message if not integer first', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall("", 1)
                assert.equal(expected , actual)
            });
            it('should return error message if not integer second', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1, "")
                assert.equal(expected , actual)
            });
            it('should return error message if first < 0', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(-1, 1)
                assert.equal(expected , actual)
            });
            it('should return error message if second < 0', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1, -1)
                assert.equal(expected , actual)
            });
            it('should return error message if second = 0', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1, 0)
                assert.equal(expected , actual)
            });
            it('should return error message if first = 0', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(0, 1)
                assert.equal(expected , actual)
            });
            it('should return error message if first > 20', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(21, 1)
                assert.equal(expected , actual)
            });
            it('should return error message if second > 20', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1, 21)
                assert.equal(expected , actual)
            });
            it('should return error message if first == second', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1, 1)
                assert.equal(expected , actual)
            });
            it('should return error message if first float', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1.1, 1)
                assert.equal(expected , actual)
            });
            it('should return error message if second float', function () {
                let expected = "Unsuccessful change of seats in the hall.";
                let actual = cinema.swapSeatsInHall(1, 1.1)
                assert.equal(expected , actual)
            });
        })
        it('should return success if valid data', function () {
            let expected = "Successful change of seats in the hall.";
            let actual = cinema.swapSeatsInHall(2, 1)
            assert.equal(expected , actual)
        });
        it('should return success if valid data', function () {
            let expected = "Successful change of seats in the hall.";
            let actual = cinema.swapSeatsInHall(20, 1)
            assert.equal(expected , actual)
        });
        it('should return success if valid data', function () {
            let expected = "Successful change of seats in the hall.";
            let actual = cinema.swapSeatsInHall(1, 20)
            assert.equal(expected , actual)
        });
    })
})

