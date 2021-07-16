function solve() {
    document.querySelector('#btnSend').addEventListener('click', onClick);

    function onClick() {
        let result = []
        let allData = JSON.parse(document.getElementsByTagName('textarea')[0].value)
        for (const data of allData) {
            let [restaurantName, workers] = data.split(' - ')
            workers = workers.split(', ')
            let listOfWorkers = workers.reduce((acc, cur) => {
                let [workerName, workerSalary] = cur.split(' ')
                workerSalary = Number(workerSalary)
                acc.push({workerName, workerSalary})
                return acc
            }, [])
            if (checkForSameRestaurant(result, restaurantName)) {
                let initialObj = returnObject(result, restaurantName)
                listOfWorkers.forEach( el => initialObj.listOfWorkers.push(el))
                initialObj.maxPayment = getMaxPayment(initialObj.listOfWorkers)
                initialObj.averageSalary = getAverageSalary(initialObj.listOfWorkers)
            } else {
                let obj = {listOfWorkers,
                    restaurantName,
                    maxPayment : getMaxPayment(listOfWorkers).toFixed(2),
                    averageSalary : getAverageSalary(listOfWorkers).toFixed(2)
                }
                result.push(obj)
            }
        }
        let finalObject = findRestaurantWithMaxAverageSalary(result)
        finalObject.listOfWorkers.sort((cur, next) => cur.salary - next.salary)
        document.querySelectorAll('#bestRestaurant p')[0].textContent = `Name: ${finalObject.restaurantName} Average Salary: ${finalObject.averageSalary} Best Salary: ${finalObject.maxPayment}`
        document.querySelectorAll('#workers p')[0].textContent = finalObject.listOfWorkers.reduce((ac , cur) => {
            ac.push(`Name: ${cur.workerName} With Salary: ${cur.workerSalary}`)
            return ac
        }, []).join(' ')
    }


    function findRestaurantWithMaxAverageSalary(listOfObjects){
        let max = 0
        let cur
        for (const listOfObject of listOfObjects) {
            if(listOfObject.averageSalary > max){
                cur = listOfObject
                max = listOfObject.averageSalary
            }
        }
        return cur
    }

    function getMaxPayment(massive) {
        let max = 0
        for (const obj of massive) {
            if (obj.workerSalary > max) {
                max = obj.workerSalary
            }
        }
        return max

    function returnObject(ls, nameOfRestaurant) {
        return ls.filter(obj => obj.restaurantName === nameOfRestaurant)[0]
    }
    }

    function getAverageSalary(massive) {
        return massive.reduce((acc, cur) => {
            return acc + cur.workerSalary
        }, 0) / massive.length

    }

    function checkForSameRestaurant(ls, nameOfRestaurant) {
        return ls.filter(el => el.restaurantName === nameOfRestaurant).length === 1
    }
}