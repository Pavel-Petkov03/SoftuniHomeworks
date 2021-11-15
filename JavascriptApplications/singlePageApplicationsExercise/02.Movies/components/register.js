import {register} from "../eventListeners.js"
import {e} from "../../utils.js"
export function registerComponent(){
    const registerButton = e("button", {type : "submit", className : "btn btn-primary", textContent : "Register"})
    registerButton.addEventListener("click", register)
    return e("section" , {id : "form-sign-up"}, [
        e("form", {className : "text-center border border-light p-5", method : "post", action : void(0)},[
            e("div" , {className: "form-group"}, [
                e("label", {htmlFor : "email", textContent : "Email"}),
                e("input", {id: "email", type : "email", className : "form-control", placeholder : "Email", name : "email"})
            ]),
            e("div" , {className: "form-group"}, [
                e("label", {htmlFor : "password", textContent : "Password"}),
                e("input", {id: "password", type : "password", className : "form-control", placeholder : "Password", name : "password"})
            ]),
            e("div" , {className: "form-group"}, [
                e("label", {htmlFor : "repeatPassword", textContent : "Repeat password"}),
                e("input", {id: "repeatPassword", type : "password", className : "form-control", placeholder : "Repeat-Password", name : "repeatPassword"})
            ]),
            registerButton
        ])
    ])
}


