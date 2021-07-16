function solve() {
    document.querySelector('#btnSend').addEventListener('click', onClick);

    function onClick() {
        let result = {}
        const allData = JSON.parse(document.querySelectorAll('#inputs textarea')[0].value)
        allData.forEach(el => {
            let [name, workersWithSalaryString] = el.split(' - ')
            let listOfWorkersAsObjects = workersWithSalaryString.split(', ').reduce((ac, cur) => {
                let [name , salary] = cur.split(' ')
                salary = Number(salary)
                ac.push({name, salary})
                return ac
            },[])
            if(result[name]){
                listOfWorkersAsObjects = result[name].listOfWorkersAsObjects.concat(listOfWorkersAsObjects)
            }
            listOfWorkersAsObjects.sort((worker1, worker2) => worker2.salary- worker1.salary)
            const maxSalary = listOfWorkersAsObjects[0].salary
            const averageSalary = listOfWorkersAsObjects.reduce((ac , cur) => ac + cur.salary, 0) / listOfWorkersAsObjects.length
            result[name] = {listOfWorkersAsObjects, maxSalary, averageSalary}
        })
        let max = 0
        let bestRestaurant
        for (const name in result) {
            if(result[name].maxSalary > max){
                max = result[name].maxSalary
                bestRestaurant = {
                    name, ...result[name]
                }
            }
        }
        document.querySelector('#bestRestaurant p').textContent = `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.averageSalary.toFixed(2)} Best Salary: ${bestRestaurant.maxSalary.toFixed(2)}`
        document.querySelector('#workers p').textContent = bestRestaurant.listOfWorkersAsObjects.map(el => `Name: ${el.name} With Salary: ${el.salary}`).join(' ')
    }
}