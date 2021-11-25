import {html} from "../src.js" 


export const furnitureTemplate = (data, isAuthenticated) => html `
    <div class="col-md-4">
                    <div class="card text-white bg-primary">
                        <div class="card-body">
                                <img src="${data.img}" />
                                <p>Description here</p>
                                <footer>
                                    <p>Price: <span>"${data.price}" $</span></p>
                                </footer>
                                ${isAuthenticated !== null ? html`<div>
                                    <a href="/details/${data._id}" class="btn btn-info">Details</a>
                                </div>` : null}
                        </div>
                    </div>
                </div>
`