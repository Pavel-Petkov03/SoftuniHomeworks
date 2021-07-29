function solve(area, vol, input) {
    let array = JSON.parse(input)
    let finalArray = []
    array.forEach(obj => {
        finalArray.push(
            {
                area: area.call(obj),
                volume: vol.call(obj)
            }
        )
    })

    return finalArray
}


function vol() {
    return Math.abs(this.x * this.y * this.z);
}


function area() {
    return Math.abs(this.x * this.y);
}


// second


function increaseFunction(currentNumber) {
    function increase(number) {
        return currentNumber + number
    }

    return increase
}


// third

function createFormatter(separator, symbol, symbolFirst, formatter) {
    return formatter.bind(null, separator, symbol, symbolFirst)
}

function currencyFormatter(separator, symbol, symbolFirst, value) {
    let result = Math.trunc(value) + separator;
    result += value.toFixed(2).substr(-2, 2);
    if (symbolFirst) return symbol + ' ' + result;
    else return result + ' ' + symbol;
}


// forth


function filterEmployees(json, argument) {
    let [key, value] = argument.split('-')
    let employeesArray = JSON.parse(json)
    if (argument === 'all') {
        printAllEmployees(employeesArray)
    } else {
        let filteredArray = employeesArray.filter(obj => filter(key, value, obj))
        printAllEmployees(filteredArray)
    }


    function filter(key, value, obj) {
        return value === obj[key]
    }

    function printAllEmployees(array) {
        let place = 0
        array.forEach(obj => {
            console.log(`${place}. ${obj.first_name} ${obj.last_name} - ${obj.email}`)
            place++
        })
    }
}



// fifth


function solution() {
    let string = ''

    function append(str) {
        string += str
    }

    function removeStart(n) {
        string = string.split('').slice(n).join('')
    }

    function removeEnd(n) {
        string = string.split('').slice(0, string.length - n).join('')
    }

    function print() {
        console.log(string)
    }

    return {
        append,
        removeStart,
        removeEnd,
        print
    }
}

// sixth

function listProcessor(array) {
    let finalArray = []

    function print() {
        console.log(finalArray.join())
    }

    function add(el) {
        finalArray.push(el)
    }

    function remove(el) {
        for (const element of finalArray) {
            if (element === el){
                 finalArray.splice(el, 1)
            }
        }

    }

    array.forEach(str => {
        let [type, value] = str.split(' ')
        switch (type) {
            case 'add':
                add(value);
                break
            case 'remove' :
                remove(value);
                break
            case 'print' :
                print();
                break
        }
    })
}

// seventh


function cars(array) {
    let objects = {}
    let finalObjects = {}
    array.forEach(command => {
        let splitCommand = command.split(' ')
        let initialName = splitCommand[1]
        if (splitCommand.length === 2 && splitCommand[0] === 'create') {
            objects[initialName] = {listOfChildren: []}
            finalObjects[initialName] = objects[initialName]
        } else if (splitCommand.length === 4 && splitCommand[2] === 'inherit') {
            objects[splitCommand[3]].listOfChildren.push({initialName})
            finalObjects[splitCommand[3]] = objects[splitCommand[3]]
        } else if (splitCommand.length === 4) {
            let [_, name, key, value] = splitCommand
        } else {

        }
    })
}




