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