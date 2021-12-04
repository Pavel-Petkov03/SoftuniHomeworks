import { html } from "../lib.js"
import { getUserInfo } from "../utils.js"


export const  articleTemplate = (data) => html`
<div class="card-box">
                <img src=${data.imgUrl}>
                <div>
                    <div class="text-center">
                        <p class="name">Name: ${data.name}</p>
                        <p class="artist">Artist: ${data.artist}</p>
                        <p class="genre">Genre: ${data.genre}</p>
                        <p class="price">Price: ${data.price}</p>
                        <p class="date">Release Date: ${data.releaseDate}</p>
                    </div>
                </div>
                ${getUserInfo() ? html`<div class="btn-group">
                        <a href="/details/${data._id}" id="details">Details</a>
                </div>`  : null}
                
            </div>
`