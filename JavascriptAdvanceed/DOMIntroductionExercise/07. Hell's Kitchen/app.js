function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let result = []
      let allData = JSON.parse(document.getElementsByTagName('textarea')[0].value)
      allData.forEach(el => {
         let [nameOfRestaurant , data] = el.split(' - ')
         let listOfWorkers = data.split(', ')
         let listOfBestRestaurantWorkers = []
         let salaryList = []

         listOfWorkers.forEach(workerWithSalary => {
            let [workerName , workerSalary] = workerWithSalary.split(' ')
            workerSalary = parseFloat(workerSalary)
            salaryList.push(workerSalary)
            listOfBestRestaurantWorkers.push({workerName, workerSalary})
         })

         listOfBestRestaurantWorkers.sort((cur, next) => {
            return next.workerSalary - cur.workerSalary}).forEach((obj, index , array) =>
         {array[index] = `Name: ${obj.workerName} With Salary: ${obj.workerSalary}`})

         let bestSalary = Math.max(...salaryList).toFixed(2)
         let averageSalary = (salaryList.reduce((acc , cur) => acc+cur, 0) / salaryList.length).toFixed(2)
         result.push({nameOfRestaurant, listOfBestRestaurantWorkers, bestSalary , averageSalary})
      })

      function findBestSalary(arrayOfObjects){
         let maxFind = 0
         let wantedObject
         for (const arrayOfObject of arrayOfObjects) {
            let salary = arrayOfObject.bestSalary
            if(salary >  maxFind){
               wantedObject = arrayOfObject
            }
         }
         return wantedObject
      }

      let newAssign = findBestSalary(result)
      let bestRestaurantArea = document.querySelector('#bestRestaurant p')
      let bestWorkersArea = document.querySelector('#workers p')
      bestRestaurantArea.textContent = `Name: ${newAssign.nameOfRestaurant} Average Salary: ${newAssign.averageSalary} Best Salary: ${newAssign.bestSalary}`
      bestWorkersArea.textContent = newAssign.listOfBestRestaurantWorkers.join(' ')
   }
}
