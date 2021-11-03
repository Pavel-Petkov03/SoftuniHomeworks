function sort(array, task) {
    function ascending() {
        return array.sort((current, next) =>
            Number(current) - Number(next)
        )
    }

    function descending() {
        return array.sort((current, next) =>
            Number(next) - Number(current)
        )
    }

    switch (task) {
        case  'desc' :
            return descending()
        case  'asc' :
            return ascending()
    }
}





