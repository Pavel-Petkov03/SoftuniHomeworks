function fruit(string, grams, price) {
    grams /= 1000
    console.log(`I need $${(price * grams).toFixed(2)} to buy ${grams.toFixed(2)} kilograms ${string}.`)
}

function biggestDivisor(first, second) {
    let maxDev;
    for (let i = 1; i <= Math.max(first, second); i++) {
        if (first % i === 0 && second % i === 0) {
            maxDev = i
        }
    }
    console.log(maxDev)
}


function sameNumbers(string) {
    string = String(string)
    let list = string.split('')
    console.log(list.filter((x => x === list[0])).length === list.length ? 'true' : 'false')
    console.log(list.reduce((a, b) => (a + parseInt(b)), 0))
}


function solveTime(steps, footstep, kmPerHour) {
    let meters = steps * footstep
    let additionalMinutes = Math.floor(meters / 500)
    let km = meters / 1000
    let hours = km / kmPerHour
    let seconds = hours * 3600 + 60 * additionalMinutes
    let finalHours = Math.floor(hours) <= 9 ? `0${Math.floor(hours)}` : `${Math.floor(hours)}`
    let finalMinutes = Math.floor(seconds / 60) <= 9 ? `0${Math.floor(seconds / 60)}` : `${Math.floor(seconds / 60)}`
    let finalSeconds = seconds % 60 <= 9 ? `0${(seconds % 60).toFixed()}` : `${(seconds % 60).toFixed()}`
    console.log(`${finalHours}:${finalMinutes}:${finalSeconds}`)
}


function cookingNumbers(num, task1, task2, task3, task4, task5) {
    let myList = [task1, task2, task3, task4, task5]
    let initialNum = parseInt(num)
    for (const task of myList) {
        switch (task) {
            case 'chop' :
                initialNum *= 0.5;
                break
            case 'dice' :
                initialNum = Math.sqrt(initialNum);
                break
            case 'spice' :
                initialNum++;
                break
            case 'bake' :
                initialNum *= 3;
                break
            case 'fillet' :
                initialNum *= 0.8;
                break
        }
        console.log(initialNum)
    }
}




function validityChecker(x1, y1, x2, y2) {
    let distanceFromX1ToZero = Math.sqrt(x1**2 + y1**2)
    let distanceFromX2ToZero = Math.sqrt(x2**2 + y2**2)
    if (Math.floor(distanceFromX1ToZero) === distanceFromX1ToZero){
        console.log(`{${x1}, ${y1}} to {${0}, ${0}} is valid`)
    }else{
        console.log(`{${x1}, ${y1}} to {${0}, ${0}} is invalid`)
    }
    if (Math.floor(distanceFromX2ToZero) === distanceFromX2ToZero){
        console.log(`{${x2}, ${y2}} to {${0}, ${0}} is valid`)
    }else{
        console.log(`{${x2}, ${y2}} to {${0}, ${0}} is invalid`)
    }
    let xDistance = x1 >= x2 ? x1 - x2 :  x2 - x1
    let yDistance = y1 >= y2 ? y1 - y2 :  y2 - y1
    let distance = Math.sqrt(xDistance**2 + yDistance**2)
    if(Math.floor(distance) === distance){
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`)
    }else{
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`)
    }
}

validityChecker(3, 0, 0, 4)


function roadRider(km, place) {
    let maxSpeed;
    switch (place) {
        case 'motorway':
            maxSpeed = 130;
            break;
        case 'interstate':
            maxSpeed = 90;
            break;
        case 'city':
            maxSpeed = 50;
            break;
        case 'residential':
            maxSpeed = 20;
            break;
    }
    if (km <= maxSpeed) {
        console.log(`Driving ${km} km/h in a ${maxSpeed} zone`);
    } else {
        let overDrive = km - maxSpeed;
        let status;
        if (overDrive <= 20) {
            status = 'speeding'
        } else if (overDrive <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }
        console.log(`The speed is ${overDrive} km/h faster than the allowed speed of ${maxSpeed} - ${status}`)
    }
}

function reg(sentence){
    let exp = /[A-Za-z0-9]+/gi;
    return (sentence.match(exp)).join(', ').toUpperCase()
}



