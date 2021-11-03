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