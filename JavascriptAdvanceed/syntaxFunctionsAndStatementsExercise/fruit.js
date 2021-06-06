function fruit(string , grams, price){
    console.log(`I need $${price.toFixed(2)} to buy ${grams} kilograms ${string}.`)
}

function biggestDivisor(first , second){
    let maxDev;
    for (let i = 1; i<= Math.max(first , second); i++){
        if(first % i === 0 && second % i === 0){
            maxDev = i
        }
    }
    console.log(maxDev)
}



function sameNumbers(string){
    string = String(string)
    let list = string.split('')
    console.log(list.filter((x => x === list[0])).length === list.length ? 'true': 'false')
    console.log(list.reduce((a , b) => (a+parseInt(b)), 0))
}

sameNumbers(333)


function solveTime(steps , footstep , kmPerHour){
    let meters = steps * footstep
    let additionalMinutes = Math.floor( meters/ 500)
    let km = meters / 1000
    let hours = km / kmPerHour
    let seconds = hours * 3600 + 60 * additionalMinutes
    let finalHours = Math.floor(hours) <= 9 ? `0${Math.floor(hours)}` : `${Math.floor(hours)}`
    let finalMinutes = Math.floor(seconds/ 60) <= 9 ? `0${Math.floor(seconds/ 60)}` : `${Math.floor(seconds/ 60)}`
    let finalSeconds = seconds % 60 <= 9 ? `0${(seconds % 60).toFixed()}` : `${(seconds % 60).toFixed()}`
    console.log(`${finalHours}:${finalMinutes}:${finalSeconds}`)
}




function cookingNumbers(num , task1 , task2 ,task3 ,task4 ,task5){
    let myList = [task1 , task2 , task3 , task4 , task5]
    let initialNum = parseInt(num)
    for (const task of  myList) {
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
            case 'base' :
                initialNum *= 3;
                break
            case 'fillet' :
                initialNum *= 0.8;
                break
        }
        console.log(initialNum)
    }
}

cookingNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop')


function validityChecker(x1 , y1 , x2 , y2){
    console.log(x1 == 0 || y1 == 0 ? `{${x1}, ${y1}} to {${0}, ${0}} is valid` : `{${x1}, ${y1}} to {${0}, ${0}} is invalid`)
    console.log(x2 == 0 || y2 == 0 ? `{${x2}, ${y2}} to {${0}, ${0}} is valid` : `{${x2}, ${y2}} to {${0}, ${0}} is invalid`)
    if (x1 in  [x2 , y2] || y1 in [x2 , y2] ){
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`)
    }else{
         console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`)
    }
}
validityChecker(2, 1, 1, 1)