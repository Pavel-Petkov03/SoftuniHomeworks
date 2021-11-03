class Company {

    constructor() {
        this.departments = {}
    }

    static invalidData = ["", undefined, null]

    addEmployee(name, salary, position, department) {
        if (Company.invalidData.includes(name) || Company.invalidData.includes(position) || Company.invalidData.includes(department)) {
            throw new Error("Invalid input!")
        }
        if (!salary || salary < 0) {
            throw new Error("Invalid input!")
        }

        if (!this.departments[department]) {
            this.departments[department] = []
        }
        this.departments[department].push({name, salary, position})
        return `New employee is hired. Name: ${name}. Position: ${position}`
    }

    companyAverageSalaryPair() {
        return Object.entries(this.departments).reduce((acc, cur) => {
            let average = cur[1].reduce((acc, obj) => acc + obj.salary, 0) / cur[1].length
            if (average > acc[1]) {
                cur.average = average
                acc[0] = cur[0]
                acc[1] += average
            }
            return acc
        }, ["", 0])
    }

    bestDepartment() {
        let result = []
        const [bestDepartmentName, bestDepartmentSalary] = this.companyAverageSalaryPair()
        const employeeArray = this.departments[bestDepartmentName]
        result.push(`Best Department is: ${bestDepartmentName}`, `Average salary: ${(bestDepartmentSalary).toFixed(2)}`)
        employeeArray.sort((current, next) => {
            if (next.salary !== current.salary) {
                return next.salary - current.salary
            }
            return current.name.localeCompare(next.name)
        }).forEach(({name, salary, position}) => {
            result.push(`${name} ${salary} ${position}`)
        })
        return result.join("\n")
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
