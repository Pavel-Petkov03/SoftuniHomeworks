import {login} from "../eventListeners.js"
import {e} from "../../utils.js"

export function loginComponent(){
    const loginBtn = e("button", {type : "submit", className : "btn btn-primary", textContent : "Login"})
    loginBtn.addEventListener("click", login)
    return e("section", {id : "form-login"}, [
        e("form", {className : "text-center border border-light p-5"}, [
            e("div", {className : "form-group"}, [
                e("label", {htmlFor : "email", textContent : "Email"}),
                e("input", {placeholder : "Email", id : "email", type : "email", className : "form-control", name : "email"})
            ]),
            e("div", {className : "form-group"}, [
                e("label", {htmlFor : "password", textContent : "Password"}),
                e("input", {placeholder : "Password", id : "password", type : "password", className : "form-control" , name : "password"})
            ]),
            loginBtn
        ])
    ])
}