function biggestDivisor(first, second) {
    let maxDev;
    for (let i = 1; i <= Math.max(first, second); i++) {
        if (first % i === 0 && second % i === 0) {
            maxDev = i
        }
    }
    console.log(maxDev)
}