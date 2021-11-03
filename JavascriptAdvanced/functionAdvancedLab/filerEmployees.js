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