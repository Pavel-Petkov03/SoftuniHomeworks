catFactory = (obj) => {
    let helperVolume = {
        90: 1800,
        120: 2400,
        200: 3500
    }
    let helperPower = (power) => {
        if (power <= 90) {
            return 90
        } else if (power <= 120) {
            return 120
        }
        return 200
    }
    let wheels = (obj) => {
        let wheelSize = Math.floor(obj.wheelsize)
        if (wheelSize % 2 === 0) {
            wheelSize--
        }
        wheelSize = Math.floor(wheelSize)
        return [wheelSize, wheelSize, wheelSize, wheelSize]
    }


    return {
        model: obj.model,
        engine: {
            power: helperPower(obj.power),
            volume: helperVolume[helperPower(obj.power)]
        },
        carriage: {
            type: obj.carriage,
            color: obj.color
        },
        wheels: wheels(obj)

    }
}