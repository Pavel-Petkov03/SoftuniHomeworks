class Point {
    constructor(x, y) {
        this.x = x
        this.y = y
    }

    static distance(pointOne , pointTwo){
        return Math.sqrt(Math.pow((pointOne.x - pointTwo.x), 2) + Math.pow((pointOne.y - pointTwo.y), 2))
    }
}


const a = new Point(1 , 2)
const b = new Point(5 , 5)

console.log(
    Point.distance(a , b)
)
