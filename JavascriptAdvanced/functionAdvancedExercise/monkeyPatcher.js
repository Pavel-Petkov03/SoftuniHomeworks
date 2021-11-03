function solution(task) {
    let rating = ''
    let allVotes = this.upvotes + this.downvotes
    let balance = this.upvotes - this.downvotes
    switch (task) {
        case 'upvote' :
            this.upvotes++;
            break
        case 'downvote' :
            this.downvotes++;
            break
        case 'score' :
            if(allVotes < 10){
                 rating = 'new'
            }
            else if (this.upvotes > allVotes * 0.66) {
                rating = 'hot'
            } else if (allVotes > 100 && balance >= 0) {
                rating = 'controversial'
            } else if (balance < 0) {
                rating = 'unpopular'
            } else {
                rating = 'new'
            }
            let final = [this.upvotes, this.downvotes, balance, rating]
            if (allVotes > 50) {
                let value = Math.ceil(Math.max(this.upvotes , this.downvotes)* 0.25)
                final[0] += value
                final[1] += value
            }
            return final
    }

}