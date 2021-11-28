import {html, render} from "../lib.js"
import { getUserInfo } from "../utils.js"
const template = (data) => html`
            <nav>
            <a href="/browse" class="action">Browse Teams</a>
                ${data ?  html`<a href="/my-profile/${data._id}" class="action">My Teams</a><a href="#" class="action">Logout</a>` 
                : html`<a href="/login" class="action">Login</a><a href="/register" class="action">Register</a>`}
            </nav>
`
export function renderNav(){
    render(template(getUserInfo()), document.querySelector("header"))
}