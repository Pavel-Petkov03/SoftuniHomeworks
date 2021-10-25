class Person {
    constructor(firstName, lastName, age, email) {
        this.lastName = lastName;
        this.firstName = firstName
        this.age = age
        this.email = email
    }

    toString() {
        return `${this.firstName} ${this.lastName} (age: ${this.age}, email: ${this.email})`
    }
}

const person1 = new Person("Anna", "Simpson", 22, "anna@yahoo.com")
const person2 = new Person("Softuni" , "", "" , "")
const person3 = new Person("Softuni" , "", "" , "")
const person4 = new Person("Softuni" , "", "" , "")

function getPersons(persons){
    return persons
}

console.log(
    getPersons(
        [person3 , person4 , person2 , person1]
    )
)