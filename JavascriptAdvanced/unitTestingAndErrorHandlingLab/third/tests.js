const {rgbToHexColor} = require("../third/rgbToHex")
const {assert} = require("chai")

// red , green,  blue
describe("Testing" , () => {
    it('should return undefined if colors not in boundaries or not numbers', function () {
        // test red not good type
        assert.equal(rgbToHexColor("z" , 1,1), undefined)
        assert.equal(rgbToHexColor([] , 1,1), undefined)
        assert.equal(rgbToHexColor({} , 1,1), undefined)
        assert.equal(rgbToHexColor(1.1 , 1,1), undefined)
        assert.equal(rgbToHexColor(null , 1,1), undefined)
        assert.equal(rgbToHexColor(undefined , 1,1), undefined)
        // test red not in boundaries
        assert.equal(rgbToHexColor(256 , 1,1), undefined)
        assert.equal(rgbToHexColor(-1 , 1,1), undefined)

        // test blue not good type
        assert.equal(rgbToHexColor(1 , "z",1), undefined)
        assert.equal(rgbToHexColor(1 , [],1), undefined)
        assert.equal(rgbToHexColor(1 , {},1), undefined)
        assert.equal(rgbToHexColor(1 , 1.1,1), undefined)
        assert.equal(rgbToHexColor(1 , null,1), undefined)
        assert.equal(rgbToHexColor(1 , undefined,1), undefined)
        // test red not in boundaries
        assert.equal(rgbToHexColor(1 , 256,1), undefined)
        assert.equal(rgbToHexColor(1 , -1,1), undefined)
        assert.equal(rgbToHexColor(1 , 1.1,1), undefined)

        // test blue not good type
        assert.equal(rgbToHexColor(1 , 1,"z"), undefined)
        assert.equal(rgbToHexColor(1 , 1,[]), undefined)
        assert.equal(rgbToHexColor(1 , 1,{}), undefined)
        assert.equal(rgbToHexColor(1 , 1,1.1), undefined)
        assert.equal(rgbToHexColor(1 , 1,null), undefined)
        assert.equal(rgbToHexColor(1 , 1,undefined), undefined)
        // test red not in boundaries
        assert.equal(rgbToHexColor(1 , 1,256), undefined)
        assert.equal(rgbToHexColor(1 , 1,-1), undefined)

    });
    it('should return hex if valid arguments', function () {
        assert.equal(rgbToHexColor(1,1,1) , "#010101")
        assert.equal(rgbToHexColor(255,255,255) , "#FFFFFF")
        assert.equal(rgbToHexColor(0,0,0) , "#000000")
        assert.equal(rgbToHexColor(123,54,12) , "#7B360C")
    });
})