function e(type, attributes, children) {
    let result = document.createElement(type)
    if (Object.values(attributes).length > 0) {
        Object.entries(attributes).forEach(([prop, val]) => {
            result[prop] = val
        })
    }
    if (children) {
        children.forEach(el => {
            if(el){
                result.appendChild(el)
            }
        })
    }
    return result
}

async function generateRequest(uri, method, body, token) {
    let init = {headers: {"content-type": "application/json"}}
    init.method = method

    if (body) {
        init.body = JSON.stringify(body)
    }
    if (token) {
        init.headers["x-authorization"] = token
    }
    let res = await fetch(uri, init)
    let data = await res.json()
    if (data.hasOwnProperty("message")) {
        throw new Error(data.message)
    }
    return data
}

function retrieveData(form) {
    let data = new FormData(form)
    let result = [...data.entries()].reduce((acc, cur) => {
        let [prop, val] = cur
        acc[prop] = val
        return acc
    }, {})
    cleanData(form)
    return result
}
function validate(email , password , repeatPassword){
    let message
    if (email === ""){
        message = "email must be filled"
    }else if(password.length <6){
        message = "password must be at least 6 characters"
    }else if(password !== repeatPassword){
        message = "password must match confirm password"
    }
    if(message){
        throw new Error(message)
    }
}

function cleanData(form){
    form.reset()
}

export {
    generateRequest, e, retrieveData, cleanData, validate
}