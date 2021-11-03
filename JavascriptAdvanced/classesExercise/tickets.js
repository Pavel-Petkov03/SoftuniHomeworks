

function solve(array , sortingString){
    class Ticket{
        constructor(destination, price, status) {
            this.destination = destination
            this.status = status
            this.price = Number(price)
        }

        static makeTickets(array) {
            return array.reduce((acc, cur) => {
                let [destination, price, status] = cur.split("|")
                price = Number(price)
                acc.push(new Ticket(destination , price , status))
                return acc
            }, [])
        }

        static sortedArray(reducedArray , sortingString){
            switch (sortingString){
                case "destination" : return reducedArray.sort((current , next) => current.destination.localeCompare(next.destination));
                case "status" : return reducedArray.sort((current , next) => current.status.localeCompare(next.status));
                case "price" : return reducedArray.sort((current , next) => current.price - next.price);
            }
        }
    }
    const reducedArray = Ticket.makeTickets(array)
    return Ticket.sortedArray(reducedArray , sortingString)
}



