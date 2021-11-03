class Stringer {
    constructor(string, length) {
        this.innerString = string
        this.innerLength = length
        this.list = string.split("")
    }

    increase(number) {
        this.innerLength += number
        this.newString()
    }

    decrease(number) {

        this.innerLength -= number
        if (this.innerLength < 0) {
            this.innerLength = 0
        }
        this.newString()
    }

    newString() {
        this.innerString = this.innerLength > this.innerString.length ? this.list.join("") : this.list.slice(0, this.innerLength).join("") + "..."
    }

    toString() {
        return this.innerString
    }

}

let test = new Stringer("Test", 5);
console.log(test.toString()); // Test

test.decrease(3);
console.log(test.toString()); // Te...

test.decrease(5);
console.log(test.toString()); // ...

test.increase(4)
console.log(test.toString()); // Test
