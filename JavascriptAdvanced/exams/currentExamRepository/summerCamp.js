class SummerCamp{
    constructor(organizer , location) {
        this.organizer=  organizer
        this.location = location
        this.priceForTheCamp = {"child": 150, "student": 300, "collegian": 500}
        this.listOfParticipants = []
    }

    registerParticipant(name, condition, money){
        if(!Object.keys(this.priceForTheCamp).includes(condition)){
            throw new Error("Unsuccessful registration at the camp.")
        }
        const filter = this.listOfParticipants.filter(el => el.name === name)
        if(filter.length !== 0){
            return `The ${name} is already registered at the camp.`
        }
        if(money >= this.priceForTheCamp[condition]){
            this.listOfParticipants.push({
                name , condition , power : 100, wins : 0
            })
            return `The ${name} was successfully registered.`
        }
        return `The money is not enough to pay the stay at the camp.`
    }

    unregisterParticipant (name){
        const filter = this.listOfParticipants.filter(el => el.name === name)
        if(filter.length === 0){
            throw new Error(`The ${name} is not registered in the camp.`)
        }
        this.listOfParticipants = this.listOfParticipants.filter((el) => el!== filter[0])
        return `The ${name} removed successfully.`
    }

    timeToPlay (typeOfGame, participant1, participant2){
        const firstPlayer = this.listOfParticipants.filter(el => el.name === participant1)[0]
        const secondPlayer = this.listOfParticipants.filter(el => el.name === participant2)[0]
        let final
        if(typeOfGame === "WaterBalloonFights"){
            if(!(typeof firstPlayer === "object" && typeof secondPlayer === "object")){
                throw new Error(`Invalid entered name/s.`)
            }
            if(firstPlayer.condition !== secondPlayer.condition){
                throw new Error(`Choose players with equal condition.`)
            }
            if(firstPlayer.power > secondPlayer.power){
                final = firstPlayer
            }else if(secondPlayer.power > firstPlayer.power){
                final = secondPlayer
            }
            if(firstPlayer.power === secondPlayer.power){
                return `There is no winner.`
            }else{
                final.wins++
                return `The ${final.name} is winner in the game ${typeOfGame}.`
            }
        }else{
            if(typeof firstPlayer !== "object"){
                throw new Error(`Invalid entered name/s.`)
            }
            firstPlayer.power += 20
            return `The ${firstPlayer.name} successfully completed the game ${typeOfGame}.`
        }
    }
    toString(){
        return this.listOfParticipants.sort((cur, next) => {
            return next.wins - cur.wins
        }).reduce((acc , cur) => {
            acc.push(`${cur.name} - ${cur.condition} - ${cur.power} - ${cur.wins}`)
            return acc
        }, [`${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`]).join("\n")
    }
}

const summerCamp = new SummerCamp("Jane Austen", "Pancharevo Sofia 1137, Bulgaria");
console.log(summerCamp.registerParticipant("Petar Petarson", "student", 300));
console.log(summerCamp.timeToPlay("Battleship", "Petar Petarson"));
console.log(summerCamp.registerParticipant("Sara Dickinson", "child", 200));
console.log(summerCamp.registerParticipant("Dimitur Kostov", "student", 300));
console.log(summerCamp.timeToPlay("WaterBalloonFights", "Petar Petarson", "Dimitur Kostov"));

console.log(summerCamp.toString());
