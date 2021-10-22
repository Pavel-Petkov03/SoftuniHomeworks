function getArticleGenerator(articles) {
    function main(){
        if(articles.length > 0){
            let text = articles.shift()
        let article = document.createElement('article')
        article.textContent = text
        document.getElementById('content').appendChild(article)
        }
    }
    return main
}
