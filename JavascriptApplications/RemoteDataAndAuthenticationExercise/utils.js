function e(type, attributes, children) {
    let result = document.createElement(type)
    if (Object.values(attributes).length > 0) {
        Object.entries(attributes).forEach(([prop, val]) => {
            result[prop] = val
        })
    }
    if (children) {
        children.forEach(el => result.appendChild(el))
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
    form.reset()
    return result
}
function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}


function validateUser(password , confirmPassword , email){
    let errorMessage = ""
    if(password !== confirmPassword){
        errorMessage = "the password and repeat password must match"
    }else if(password.length <= 10 || password.length >= 20){
        errorMessage = "the password must be between 10 and 20 symbols"
    }else if(!validateEmail(email)){
        errorMessage = "the email should be valid"
    }
    if (errorMessage){
        throw new Error(errorMessage)
    }
}

export {
    generateRequest, e, retrieveData, validateUser
}