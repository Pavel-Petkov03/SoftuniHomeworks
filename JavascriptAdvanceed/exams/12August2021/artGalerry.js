class ArtGallery {
    constructor(creator) {
        this.creator = creator
        this.possibleArticles = {"picture": 200, "photo": 50, "item": 250}
        this.listOfArticles = []
        this.guests = []
    }

    addArticle(a, articleName, quantity) {
        let articleModel = a.toLowerCase()
        if (!Object.keys(this.possibleArticles).includes(articleModel)) {
            throw new Error("This article model is not included in this gallery!")
        }
        const filter = this.listOfArticles.filter(obj => obj.articleModel === articleModel && obj.articleName === articleName)
        if (filter.length > 0) {
            filter[0].quantity += quantity
        } else {
            this.listOfArticles.push({articleName, articleModel, quantity})
        }

        return `Successfully added article ${articleName} with a new quantity- ${quantity}.`
    }

    inviteGuest(guestName, personality) {
        const pointObject = {
            "Vip": 500,
            "Middle": 250
        }
        const filter = this.guests.filter(obj => obj.guestName === guestName)
        if (filter.length > 0) {
            throw new Error(`${guestName} has already been invited.`)
        } else {
            let points
            if (Object.keys(pointObject).includes(personality)) {
                points = pointObject[personality]
            } else {
                points = 50
            }
            this.guests.push({guestName, points, purchaseArticle: 0})
            return `You have successfully invited ${guestName}!`
        }
    }

    buyArticle(articleModel, articleName, guestName) {
        const filterArticle = this.listOfArticles.filter(obj => obj.articleModel === articleModel && obj.articleName === articleName)
        const article = filterArticle[0]
        if (!Object.keys(this.possibleArticles).includes(articleModel) || filterArticle.length === 0) {
            throw new Error("This article is not found.")
        }
        if (article.quantity === 0) {
            return `The ${articleName} is not available.`
        }
        const filterGuest = this.guests.filter(obj => obj.guestName === guestName)
        if (filterGuest.length === 0) {
            return "This guest is not invited."
        }
        let guest = filterGuest[0]
        if (guest.points >= this.possibleArticles[article.articleModel]) {
            guest.points -= this.possibleArticles[article.articleModel]
            guest.purchaseArticle++
            article.quantity--
            return `${guestName} successfully purchased the article worth ${this.possibleArticles[article.articleModel]} points.`
        } else {
            return "You need to more points to purchase the article."
        }
    }

    showGalleryInfo(criteria) {
        let result = []
        switch (criteria) {
            case "article" :
                result.push("Articles information:")
                this.listOfArticles.forEach((el) => result.push(`${el.articleModel} - ${el.articleName} - ${el.quantity}`));
                break
            case "guest" :
                result.push("Guests information:")
                this.guests.forEach((el) => result.push(`${el.guestName} - ${el.purchaseArticle}`));
                break
        }

        return result.join("\n")
    }
}



const artGallery = new ArtGallery('Curtis Mayfield');
artGallery.addArticle('picture', 'Mona Liza', 3);
artGallery.addArticle('Item', 'Ancient vase', 2);
artGallery.addArticle('picture', 'Mona Liza', 1);
artGallery.inviteGuest('John', 'Vip');
artGallery.inviteGuest('Peter', 'Middle');
artGallery.buyArticle('picture', 'Mona Liza', 'John');
artGallery.buyArticle('item', 'Ancient vase', 'Peter');
console.log(artGallery.showGalleryInfo('article'));
console.log(artGallery.showGalleryInfo('guest'));
