function listProcessor(array) {
    let finalArray = []

    function print() {
        console.log(finalArray.join())
    }

    function add(el) {
        finalArray.push(el)
    }

    function remove(el) {
        for (const element of finalArray) {
            if (element === el) {
                finalArray.splice(el, 1)
            }
        }

    }

    array.forEach(str => {
        let [type, value] = str.split(' ')
        switch (type) {
            case 'add':
                add(value);
                break
            case 'remove' :
                remove(value);
                break
            case 'print' :
                print();
                break
        }
    })
}