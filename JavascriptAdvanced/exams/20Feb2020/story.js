class Story {
    #comments;
    #likes;

    constructor(title, creator) {
        this.title = title
        this.creator = creator
        this.#comments = []
        this.#likes = []
    }

    get likes() {
        if (this.#likes.length === 0) {
            return `${this.title} has 0 likes`
        } else if (this.#likes.length === 1) {
            return `${this.#likes[0]} likes this story!`
        }
        return `${this.#likes[0]} and ${this.#likes.length - 1} others like this story!`
    }

    like(username) {
        const filter = this.#likes.filter(el => el === username)
        if (filter.length === 1) {
            throw new Error("You can't like the same story twice!")
        }
        if (filter.length === 1 || username === this.creator) {
            throw new Error("You can't like your own story!")
        }
        this.#likes.push(username)
        return `${username} liked ${this.title}!`
    }

    dislike(username) {
        const filter = this.#likes.filter(el => el === username)
        if (filter.length === 1) {
            this.#likes = this.#likes.filter(el => el !== username)
            return `${username} disliked ${this.title}`
        }
        throw new Error("You can't dislike this story!")
    }

    comment(username, content, id) {
        const filter = this.#comments.filter(el => el.id === id)
        if (id === undefined || filter.length === 0) {
            this.#comments.push({username, content, id: this.#comments.length + 1, replies: []})
            return `${username} commented on ${this.title}`
        }
        const obj = filter[0]
        const currentId = obj.id
        obj.replies.push({id: currentId + (obj.replies.length + 1) / 10, username, content})
        return "You replied successfully"
    }

    toString(sortingType) {
        let result = [`Title: ${this.title}`, `Creator: ${this.creator}`, `Likes: ${this.#likes.length}`, "Comments:"]

        function sort(cur, next) {
            switch (sortingType) {
                case "asc" :
                    return Number(cur.id) - Number(next.id);
                case "desc" :
                    return Number(next.id) - Number(cur.id);
                case "username" :
                    return cur.username.localeCompare(next.username)

            }
        }

        this.#comments.sort(sort).forEach(comment => {
            result.push(`-- ${comment.id}. ${comment.username}: ${comment.content}`)
            comment.replies.sort(sort).forEach(reply => {
                result.push(`--- ${reply.id}. ${reply.username}: ${reply.content}`)
            })
        })

        return result.join("\n")
    }
}