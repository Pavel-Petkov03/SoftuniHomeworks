import {e} from '../../utils.js'


export function footer(){
    return e("footer", {className : "page-footer font-small"}, [
        e("div", {className : "footer-copyright text-center py-3", textContent : "© 2020"}, [
            e("a", {href : void(0), className : "text-dark", textContent : "JS Applications"})
        ])
    ])
}