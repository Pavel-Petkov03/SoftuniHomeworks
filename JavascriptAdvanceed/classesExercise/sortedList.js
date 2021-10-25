class List {
    constructor() {
        this.list = []
        this.size = 0
    }

    add(number) {
        this.list.push(number)
        this.sort()
    }

    remove(index) {
        if(index >= 0 && index < this.list.length){
            this.list.splice(index, 1)
            this.sort()
        }
    }

    get(index) {
        if(index >= 0 && index < this.list.length){
            return this.list[index]
        }
    }

    sort(){
        this.list.sort((a , b) => a-b )
        this.size = this.list.length
    }
}
