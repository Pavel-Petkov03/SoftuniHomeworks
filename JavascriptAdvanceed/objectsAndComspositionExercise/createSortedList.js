createSortedList = () => {

    let array = []
    let sortArray = (array) => {
        return array.sort((a, b) => a - b)
    }

    function add(element) {
        array.push(element)
        array = sortArray(array)
        this.size++
    }

    function remove(index) {
        if (index >= 0 && index < array.length) {
            array.splice(index, 1)
            this.size--
        }

    }

    function get(index) {
        if (index >= 0 && index < array.length) {
            return array[index]
        }

    }

    return {size: 0, add, remove, get}
}