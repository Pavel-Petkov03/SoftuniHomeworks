function sortByTwoCriteria(array) {
    array.sort((current , next) => {
        if(current.length === next.length){
            return current.localeCompare(next)
        }
        return current.length - next.length
    })
    array.forEach(el => console.log(el))
}