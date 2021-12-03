
import { endpoints } from "../api.js"
import {html} from "../lib.js"
import { generateRequest } from "../utils.js"


const template = (array) => html`
<section id="welcome-world">
    <div class="welcome-message">
                <h2>ALL new games are</h2>
                <h3>Only in GamesPlay</h3>
            </div>
            <img src="./images/four_slider_img01.png" alt="hero">

            <div id="home-page">
                <h1>Latest Games</h1>
                ${array.length > 0 ? array.map(gameTemplate) : html`<p class="no-articles">No games yet</p>`}
            </div>
</section>

`

const gameTemplate = (data) => html`
    <div class="game">
                    <div class="image-wrap">
                        <img src=${data.imageUrl}>
                    </div>
                    <h3>${data.title}</h3>
                    <div class="rating">
                        <span>☆</span><span>☆</span><span>☆</span><span>☆</span><span>☆</span>
                    </div>
                    <div class="data-buttons">
                        <a href="/details/${data._id}" class="btn details-btn">Details</a>
                    </div>
                </div>
`




async function getAllGames(){
    const data = await generateRequest(endpoints.catalog , "get")
    return data
}
export async function renderWelcomePage(ctx){
    ctx.render(template(await getAllGames()))
}