function getFibonator() {
    let n = 0
    let cur = 0
    let next = 0

    function increase() {
        n++
        if (n === 1) {
            next = 1;
            return 1
        }
        let temp = next
        next += cur
        cur = temp
        return next
    }

    return increase
}